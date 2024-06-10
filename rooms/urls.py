from django.urls import path
from .  import views

app_name = "rooms"

# urlpatterns = [
#     # path("detail/<slug:slug>/room-type/<slug:rt-slug>/", views.room_type_detail, name="room_type_detail"),
#     path("detail/<slug>", views.room_type_detail, name ="room_type_detail"),
# ]
urlpatterns = [
    path('detail/<slug:slug>/room-type/<slug:rt_slug>', views.room_type_detail, name='room_type_detail'),
]
