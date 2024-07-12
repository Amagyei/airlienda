from django.urls import path
from . import views

app_name = 'userDashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
<<<<<<< HEAD
    path('booking-detail/<booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking-history', views.booking_history, name='booking_history'),
    path('create_complaints', views.create_complaint, name='create_complaint')
    
=======
>>>>>>> 5475ca9e7b47122f42e74df2106badf331fe6cd6
]