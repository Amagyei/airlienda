from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models

from hostel.models import Hostel, HostelFeatures, HostelGallery, HotelFaqs
from booking.models import Booking


# Create your views here.
@login_required 
def dashboard(request):
    bookings = Booking.objects.filter(user = request.user, payment_status = 'paid')
    total_spent = Booking.objects.filter(user = request.user, payment_status = 'paid').aggregate(amount = models.Sum("total"))

    context = {
        "bookings": bookings,
        "total_spent": total_spent
    }
    return render(request, "dashboard.html", context)

@login_required
def booking_detail(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id, user = request.user, payment_status = 'paid')

    context = {
        "booking": booking,
    }
    return render(request, "booking_detail.html", context)
