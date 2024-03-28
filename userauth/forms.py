from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class UserRegistrationForm(UserCreationForm):
    full_name = forms. CharField(widget=forms.TextInput(attrs={'placeholder' :"Enter Full Name", 'class': "a custom class"}))
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email','phone',  'password1', 'password2']