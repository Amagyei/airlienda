from django.urls import path
from . import views

app_name = 'userDashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('booking-detail/<booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking-history', views.booking_history, name='booking_history'),
    path('create_complaints', views.create_complaint, name='create_complaint')
    
]
from django.urls import path
from . import views

app_name = 'userDashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('booking-detail/<booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking-history', views.booking_history, name='booking_history'),
    path('create_complaints', views.create_complaint, name='create_complaint'),
    path('report_a_fault', views.report_a_fault, name='report_a_fault'),
    
]