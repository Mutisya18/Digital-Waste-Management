# region_registration/forms.py
from django import forms
from .models import Region

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name', 'overall_area', 'code']
