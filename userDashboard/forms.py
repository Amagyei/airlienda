from django import forms
from .models import complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ['title', 'message', 'room_number'] 