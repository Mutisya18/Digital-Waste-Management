from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'phone_number', 'national_id', 'date_of_birth')

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(label='Phone Number or National ID')
    password = forms.CharField(widget=forms.PasswordInput)

class RoleSwitchForm(forms.Form):
    # Add any additional fields needed for role registration
    accept_terms = forms.BooleanField(
        required=True,
        label='I accept the terms and conditions for this role'
    )
