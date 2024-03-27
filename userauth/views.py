from django.shortcuts import render
from .models import User, Profile
from userauth.forms import UserRegistrationForm

# Create your views here.

def RegisterView(request):
    form = UserRegistrationForm()
    context = {
        "form":form
    }
    return render(request, "userauths/sign-up.html")