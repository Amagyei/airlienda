from django.shortcuts import render

from hostel.models import Hostel, HostelFeatures, HostelGallery, HotelFaqs
from rooms.models import RoomType, Room
# Create your views here.


def index(request):
    hostels = Hostel.objects.filter(status = "Live")
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



