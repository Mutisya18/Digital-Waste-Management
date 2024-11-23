from django import forms
from .models import Establishment, Location, EstablishmentType

class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = ['name', 'type', 'main_plus_code', 'total_stories', 'owner_name', 'owner_phone']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['establishment', 'name', 'plus_code', 'floor']
