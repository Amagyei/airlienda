# Imports from Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.utils import timezone

# 3rd party imports
import stripe
import json
import traceback
from decimal import Decimal
from datetime import timedelta


# model imports
from hostel.models import Hostel
from rooms.models import RoomType, Room
from booking.models import Booking, Notification

# Create your views here.

# 
# Home page
# 
def index(request):
    hostels = Hostel.objects.all()
    hostels = list(hostels)
    context = {
        "hostels": hostels
    }
    return render(request, "home.html", context)

# 
# renders Hostel Detail page
# 
def HostelDetail(request, slug):
    hostel = Hostel.objects.get(status = "Live", slug=slug)
    roomtypes = RoomType.objects.filter(hostel = hostel)

    context = {
        "hostel": hostel,
        "roomtypes":roomtypes
    }
    return render(request, "hostel_detail.html", context)  

# 
# List Selected Room's Detail page
# 
def list_selected_room(request):
    if request.method == "POST":
        try:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            selection_data = request.session.get('selection_data_obj', {})

            if not selection_data:
                messages.error(request, "No room selection data found in session.")
                return redirect('hostel:list_selected_room')

            # Assuming selection_data_obj stores room details keyed by room_id
            room_id, room_selection = next(iter(selection_data.items()), (None, None))

            if not room_selection:
                messages.error(request, "Room selection data is missing.")
                return redirect('hostel:list_selected_room')

            hostel_id = room_selection.get('hostel_id')
            if not hostel_id:
                messages.error(request, "hostel_id is missing from the selection data.")
                return redirect('hostel:list_selected_room')

            try:
                hostel = Hostel.objects.get(id=hostel_id)
            except ObjectDoesNotExist:
                messages.error(request, f"No hostel found with ID {hostel_id}.")
                return redirect('hostel:list_selected_room')

            # Retrieve other needed data
            try:
                room = Room.objects.get(rid=room_id)
                room_type = RoomType.objects.get(rtid=room_selection.get('roomtype_rtid'))
            except (ValueError, ObjectDoesNotExist):
                messages.error(request, "Invalid room or room type.")
                return redirect('hostel:list_selected_room')

            booking= Booking.objects.create(
                user=request.user if request.user.is_authenticated else None,
                full_name= full_name,
                email= email,
                phone= phone,
                hostel= hostel,
                room_type= room_type,
                before_discount= room_selection.get('before_discount', 0.00),
                total= room_type.price,
                saved= room_selection.get('saved', 0.00),
                stripe_payment_intent= room_selection.get('stripe_payment_intent'),
                room_id= room_id,
            )

            return redirect('hostel:checkout', booking_id=booking.booking_id)

        except Exception as e:
            messages.error(request, f"Error processing your booking: {str(e)}")
            return redirect('hostel:list_selected_room')

    else:
        selection_data = request.session.get('selection_data_obj', {})
        if not selection_data:
            messages.warning(request, "No room selected")
            return redirect('/')

        context = {
            'data': selection_data,
            'total_selected_items': len(selection_data)
        }
        return render(request, "selected_room.html", context)


# 
# CHECKOUT VIEWS
# 


# 
# Create Checkout
# 

def checkout(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id)
    room = Room.objects.get(rid=booking.room_id)
    context = {
        "booking": booking,
        "roomtype": room.type,
        "hostel": booking.hostel,
        "room_number": room.number,
        "room_number": room.number if room else "N/A",
        "booking_total": booking.total,
        'booking_id': booking.booking_id,
        'success_id': booking.success_id,
        "stripe_publishable_key": settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, "checkout.html", context)


# 
# create checkout session
# 


@csrf_exempt
def create_checkout_session(request, booking_id):
    print("Received request method:", request.method)
    if request.method != 'POST':

        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        data = json.loads(request.body)
        # booking_id = data.get('booking_id')
        print(booking_id)

        booking = Booking.objects.get(booking_id=booking_id)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        checkout_session = stripe.checkout.Session.create(
            customer_email=booking.email,
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',  
                        'product_data': {
                            'name': booking.room_type.name,
                        },
                        'unit_amount': int(booking.total * 100),
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('hostel:payment_success', args=[booking.booking_id])) + '?session_id={CHECKOUT_SESSION_ID}&success_id='+booking.success_id+'&booking_total='+str(booking.total),
            
            cancel_url=request.build_absolute_uri(reverse('hostel:payment_failed', args=[booking.booking_id])), 
        )
        booking.payment_status = "processing"
        booking.stripe_payment_intent = checkout_session['id']
        booking.save()
        print(checkout_session.id)
        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        traceback.print_exc()  
        return JsonResponse({'error': str(e)}, status=500)
    
# 
# Checkout PAYMENT SUCCESS view
# 
def payment_success(request, booking_id):
    success_id = request.GET.get('success_id')
    booking_total = request.GET.get('booking_total')
    if success_id and booking_total:
        success_id = success_id.rstrip('/')
        booking_total = booking_total.rstrip('/')

        booking = Booking.objects.get(booking_id=booking_id, success_id = success_id)

        if booking.total == Decimal(booking_total):
            if booking.payment_status == "processing":
                booking.payment_status = "paid"
                booking.save()

                noti = Notification.objects.create(
                    type="Booking Confirmed",
                    booking = booking
                )
                if request.user.is_authenticated:
                    noti.user = request.user
                else:
                    noti.user  = None
                noti.save()

                if 'selection_data_obj' in request.session:
                    del request.session['selection_data_obj']
            else:
                messages.success(request, 'payment made already, Thank You for your patronage ')
                # return redirect('/')
        else:
            messages.errror(request, 'payment manipulation detected ')

    return render( request, "payment_success.html", {'booking': booking})
 
    # context = {
    #     'booking': booking
    # }
    # return render(request, "payment_success.html", context)


# 
# Checkout PAYMENT FAILED view
# 
def payment_failed(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id)
    context = {
        'booking': booking
    }
    return render(request, "failed.html", context)


@csrf_exempt
def update_room_status(request):
    notifications = Notification.objects.filter(type = "Booking Confirmed")

    for notification in notifications:
        booking = notification.booking
        room = Room.objects.filter(rid = booking.room_id)
        if room.status != "OCCUPIED":
            room.status = 'OCCUPIED'
            print(f'room { room.number} occupancy status has been updated')
        return HttpResponse("Room status updated.", status=200)