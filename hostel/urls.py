from django.urls import path
from hostel import views

app_name = "hostel"

urlpatterns = [
    path("hostel/", views.index , name= "hostel")
]