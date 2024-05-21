from django.shortcuts import render, redirect
from django.contrib import messages

from hostel.models import Hostel, HostelFeatures, HostelGallery, HotelFaqs
from rooms.models import RoomType, Room
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




from django.shortcuts import render, redirect
from django.contrib import messages

def list_selected_room(request):
    if 'selection_data_obj' in request.session and request.session['selection_data_obj']:
        selection_data = request.session['selection_data_obj']
        context = {
            'data': selection_data,
            'total_selected_items': len(selection_data)
        }
    else:
        messages.warning(request, "No room selected")
        return redirect('/')

    return render(request, "selected_room.html", context)
