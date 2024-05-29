from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from hostel.models import Hostel, HostelFeatures, HostelGallery, HotelFaqs
from rooms.models import RoomType, Room
from booking.models import Booking

# Create your views here.


def index(request):
    hostels = Hostel.objects.all()
    hostels = list(hostels)
    context = {
        "hostels": hostels
    }
    return render(request, "home.html", context)


def HostelDetail(request, slug):
    hostel = Hostel.objects.get(status = "Live", slug=slug)
    roomtypes = RoomType.objects.filter(hostel = hostel)

    context = {
        "hostel": hostel,
        "roomtypes":roomtypes
    }
    return render(request, "hostel_detail.html", context)  

# def list_selected_room(request):
#     if request.method == "POST":
#         try:
#             full_name = request.POST.get('full_name')
#             email = request.POST.get('email')
#             phone = request.POST.get('phone')

#             selection_data = request.session.get('selection_data_obj', {})


#             # hostel_id = selection_data.get('hostel_id')
#             # if not hostel_id:
#             #     messages.error(request, "hostel_id is missing from the session data.")
#             #     return redirect('hostel:list_selected_room')
            
#             # try:
#             #     hostel = Hostel.objects.get(id=hostel_id)
#             # except ObjectDoesNotExist:
#             #     messages.error(request, f"No hostel found with ID {hostel_id}.")
#             #     return redirect('hostel:list_selected_room')
    
#             # hostel = Hostel.objects.get(id=selection_data.get('hostel_id'))
#             # room_type = RoomType.objects.get(rtid=selection_data.get('roomtype_id'))

#             booking, created = Booking.objects.update_or_create(
#                 user=request.user if request.user.is_authenticated else None,
#                 defaults={
#                     'full_name': full_name,
#                     'email': email,
#                     'phone': phone,
#                     # 'room': room,
#                     # 'hostel': hostel,
#                     # 'room_type': room_type,
#                     'before_discount': selection_data.get('before_discount', 0.00),
#                     'total': selection_data.get('total', 0.00),
#                     'saved': selection_data.get('saved', 0.00),
#                     'stripe_payment_intent': selection_data.get('stripe_payment_intent')
#                 }
#             )


#             return redirect('hostel:checkout', booking_id=booking.booking_id)

#         except Exception as e:
#             messages.error(request, f"Error processing your booking: {str(e)}")
#             return redirect('hostel:list_selected_room')

#     else:
#         selection_data = request.session.get('selection_data_obj', {})
#         print(selection_data)
#         if not selection_data:
#             messages.warning(request, "No room selected")
#             return redirect('/')

#         context = {
#             'data': selection_data,
#             'total_selected_items': len(selection_data) if selection_data else 0
#         }
#         return render(request, "selected_room.html", context)

# def checkout(request, booking_id): 
    # booking = Booking.objects.get(booking_id = booking_id)
    # context = {
    #     "booking": booking
    # }
    # return render(request, "checkout.html", context)

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
    }
    return render(request, "checkout.html", context)
