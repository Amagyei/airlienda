from django.urls import path
from hostel import views

app_name = "hostel"

urlpatterns = [
    path('hostel/', views.index , name= "hostel"),
    path("detail/<slug>", views.HostelDetail, name ="HostelDetail"),
    path("list_selected_room/", views.list_selected_room, name="list_selected_room"),
    path("checkout/<booking_id>/", views.checkout, name="checkout"),

]