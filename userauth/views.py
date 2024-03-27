from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import User, Profile
from userauth.forms import UserRegistrationForm

# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        messages.success(request, f"Hello {full_name}, you have already  been signed up")
        return redirect("hostel:index")


    form = UserRegistrationForm(request.POST or None)
    if form.is_valid:
        form.save()
        full_name =  form.cleaned_data.get("full_name")
        phone =  form.cleaned_data.get("phone")
        email =  form.cleaned_data.get("email ")
        password =  form.cleaned_data.get("password ")

        user = authenticate(email = email, password = password)
        login(user)
        messages.success(request, f"Hello {full_name}, you have been signed up")

        profile = Profile.objects.get(user = request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()

        return redirect("hostel:index")
        

    context = {
        "form":form
    }
    return render(request, "userauth/sign-up.html", context)