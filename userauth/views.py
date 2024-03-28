from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import User, Profile
from userauth.forms import UserRegistrationForm

# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        messages.success(request, f"Hello you have already  been signed up")
        return redirect("hostel:hostel")


    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name =  form.cleaned_data.get("full_name")
        phone =  form.cleaned_data.get("phone")
        email =  form.cleaned_data.get("email")
        password =  form.cleaned_data.get("password1")

        user = authenticate(email = email, password = password)
        login(request, user)
        messages.success(request, f"Hello {full_name}, you have been signed up")

        profile = Profile.objects.get(user = request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()

        return redirect("hostel:hostel")
        

    context = {
        "form":form
    }
    return render(request, "userauth/sign-up.html", context)