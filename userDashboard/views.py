from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.db import models

from hostel.models import Hostel, HostelFeatures, HostelGallery, HotelFaqs
from booking.models import Booking
from .forms import ComplaintForm


# Create your views here.
@login_required 
def dashboard(request):
    bookings = Booking.objects.filter(user = request.user, payment_status = 'paid')
    total_spent = Booking.objects.filter(user = request.user, payment_status = 'paid').aggregate(amount = models.Sum("total"))

    context = {
        "bookings": bookings,
        "total_spent": total_spent
    }
    return render(request, "userDashboard/dashboard.html", context)

@login_required
def booking_detail(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id, user = request.user, payment_status = 'paid')

    context = {
        "booking": booking,
    }
    return render(request, "booking_detail.html", context)

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user = request.user)

    context = {
        "bookings": bookings,
    }
    return render(request, "userDashboard/userDashboard_allBookings.html", context)

def complaints(request):
    return render(request, "userDashboard/userDashboard_complaints.html")

def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your complaint has been submitted successfully!')
            return redirect('userDashboard:dashboard')  # Redirect after POST
    else:
        form = ComplaintForm()
    return render(request, 'userDashboard/userDashboard_complaints.html', {'form': form})
