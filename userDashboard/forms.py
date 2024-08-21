from django import forms
from .models import complaint, fault

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ['title', 'message', 'room_number'] 

class FaultForm(forms.ModelForm):
    class Meta:
        model = fault
        fields = ['title', 'message', 'room_number', 'room_type', 'faulty_item']