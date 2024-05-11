from django.urls import path
from . import views

app_name = "hostel"

urlpatterns = [
    path("add_to_selection/", views.add_to_selection, name="add_to_selection")
]