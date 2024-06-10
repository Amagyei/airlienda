from django.urls import path
from hostel import views

app_name = "hostel"

urlpatterns = [
    path('hostel/', views.index , name= "hostel"),
    path("detail/<slug>", views.HostelDetail, name ="HostelDetail"),
    path("list_selected_room/", views.list_selected_room, name="list_selected_room"),
    path("checkout/<booking_id>/", views.checkout, name="checkout"),
    
    
    # payment routes

    path('api/create_checkout_session/<booking_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/<booking_id>/',views.payment_success, name='payment_success'),
    path('failed/<booking_id>/',views.payment_failed, name='payment_failed'),

]