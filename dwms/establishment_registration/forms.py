from django import forms
from django.core.exceptions import ValidationError
from .models import Establishment
from region_registration.models import Region

class EstablishmentForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Select Region")

    class Meta:
        model = Establishment
        fields = ['name', 'type', 'plus_code', 'size', 'is_story_building', 'number_of_stories', 'region']
        widgets = {
            'is_story_building': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from kwargs
        super().__init__(*args, **kwargs)
        self.fields['number_of_stories'].required = False

    def clean(self):
        cleaned_data = super().clean()
        is_story_building = cleaned_data.get('is_story_building')
        number_of_stories = cleaned_data.get('number_of_stories')
        name = cleaned_data.get('name')
        region = cleaned_data.get('region')
        establishment_type = cleaned_data.get('type')

        # Validate story building fields
        if is_story_building and not number_of_stories:
            raise ValidationError("Please specify the number of stories for a story building.")
        if number_of_stories and not is_story_building:
            raise ValidationError("Please select multiple stories option for multiple story building.")

        # Check for similar establishments by the same owner
        if self.user and name and region:
            existing_establishment = Establishment.objects.filter(
                owner=self.user,
                name__iexact=name,
                region=region
            ).exclude(pk=self.instance.pk if self.instance.pk else None).first()

            if existing_establishment:
                raise ValidationError(
                    "You have already registered an establishment with this name in this region."
                )

        # Check for similar establishments by different owners
        if name and region and establishment_type:
            similar_establishments = Establishment.objects.filter(
                name__iexact=name,
                region=region,
                type=establishment_type
            ).exclude(pk=self.instance.pk if self.instance.pk else None)

            if similar_establishments.exists():
                raise ValidationError(
                    "An establishment with this name and type already exists in this region."
                )

        return cleaned_data