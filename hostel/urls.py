from django.urls import path
from hostel import views

app_name = "hostel"
name='hostel'

urlpatterns = [
    path('', views.home , name= "home"),
    path("gallery/", views.gallery, name="gallery"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    path("detail/<slug>", views.HostelDetail, name ="HostelDetail"),
    path("list_selected_room/", views.list_selected_room, name="list_selected_room"),
    path("checkout/<booking_id>/", views.checkout, name="checkout"),
    
    
    # payment routes

    path('api/create_checkout_session/<booking_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/<booking_id>/',views.payment_success, name='payment_success'),
    path('failed/<booking_id>/',views.payment_failed, name='payment_failed'),

]
