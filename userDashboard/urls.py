from django.urls import path
from . import views

app_name = 'userDashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]