from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import LoginForm


from .models import User, Profile
from userauth.forms import UserRegistrationForm

# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        messages.success(request, f"Hello you have already  been signed up")
        return redirect("hostel:home")


    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        
        full_name =  form.cleaned_data.get("full_name")
        phone =  form.cleaned_data.get("phone")
        email =  form.cleaned_data.get("email")
        password =  form.cleaned_data.get("password1")
        form.save()


        user = authenticate(username = email, password = password)
        user.save()
        login(request, user)
        messages.success(request, f"Hello {full_name}, you have been signed up")

        profile = Profile.objects.get(user = request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()

        return redirect("hostel:home")
        

    context = {
        "form":form
    }
    return render(request, "userauth/sign-up.html", context)

def loginViewTemplate(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect("hostel:home")
    
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in.")
                next_url = request.GET.get("next", "hostel:home")
                return redirect(next_url)
            else:
                messages.error(request, "Invalid email or password.")
        except Exception as e:
            # Log the exception or send it to your monitoring system
            messages.error(request, f"An error occurred: {e}")
            return redirect("userauth:sign-in")

    return render(request, "userauth/sign-in.html", {'form': form})

def LogoutView(request):
    logout(request)
    messages.success( request, "you have been logged out")
    return redirect("hostel:home")