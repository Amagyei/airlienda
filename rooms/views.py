from django.shortcuts import render
from hostel.models import Hostel
from .models import RoomType
from .models import Room
# Create your views here.
def room_type_detail(request, slug, rt_slug):
    hostel = Hostel.objects.get(slug=slug, status = "Live")
    roomtype = RoomType.objects.get(hostel = hostel,slug = rt_slug)
    rooms = Room.objects.filter(type=roomtype, status = 'VACANT')
    rooms = list(rooms)
    # id = request.GET.get("hid")
    # print(id)
    context = {
        "hostel":hostel, 
        "roomtype":roomtype,
        "rooms": rooms
    }
    return render(request, "room_type_detail.html", context )

 


