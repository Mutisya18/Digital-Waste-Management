from django import forms
from .models import Occupant
from .models import Occupant, Establishment
from region_registration.models import Region

class OccupantEnrollmentForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Select Region")
    
    class Meta:
        model = Occupant
        fields = ['region', 'establishment', 'floor_number', 'plus_code', 'occupancy_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['establishment'].queryset = Establishment.objects.filter(region_id=region_id)
            except (ValueError, TypeError):
                pass