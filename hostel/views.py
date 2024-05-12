from django.shortcuts import render, redirect
from django.contrib import messages

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



def list_selected_room(request):
    total = 0

    if 'selection_data_obj' in request.session:
        for h_id, item in request.session['selection_data_obj'].items():
            print(h_id, item )
    else:
        messages.warning( request, "no room selected")
        return redirect('/')
    
    return render(request, "selected_room.html")