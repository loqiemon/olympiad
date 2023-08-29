from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'institution_name', 'phone_number', 'email']
