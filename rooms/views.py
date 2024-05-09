from django.shortcuts import render
from hostel.models import Hostel
from .models import RoomType
from .models import Room
# Create your views here.
# def room_type_detail(request, slug):
#     roomtypes = RoomType.objects.filter(slug = slug)
#     rooms = Room.objects.filter(status = "VACANT")
#     context = {
#         "roomtypes":roomtypes,
#         "rooms": rooms
#     }
#     return render(request, "room_detail.html", context )

def RoomsList(request, slug):
    type = RoomType.objects.get(slug= slug )
    rooms = Room.objects.filter(type=type, status = "VACANT")
    context = {
        "rooms": rooms
    }
    return render(request, "room_detail.html", context)


