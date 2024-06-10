from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

from django.core.validators import EmailValidator

class LoginForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator()])
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        # As the form saves the User model, which already includes handling for phone and full_name, no need to override save unless other logic is needed.
        user = super().save(commit=commit)
        # Any other logic if needed
        return user