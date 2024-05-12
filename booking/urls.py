from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [
    path("select_room/", views.select_room, name="select_room")
]