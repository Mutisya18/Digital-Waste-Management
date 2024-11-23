from django.db import models
from region_registration.models import Region  # Import the Region model

# Create your models here.
from django.db import models
from user_registration.models import CustomUser

class Establishment(models.Model):
    ESTABLISHMENT_TYPES = [
        ('OFFICE', 'Office Building'),
        ('APARTMENT', 'Rental Apartment'),
        ('CHURCH', 'Church'),
        ('SCHOOL', 'School'),
        ('HOME', 'Personal Home'),
        ('BUSINESS', 'Business'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=ESTABLISHMENT_TYPES)
    plus_code = models.CharField(max_length=20, unique=True)
    size = models.IntegerField(help_text="Number of buildings, units, or rooms")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)  # New field
    is_story_building = models.BooleanField(default=False)
    number_of_stories = models.IntegerField(null=True, blank=True)
    establishment_id = models.CharField(max_length=10, unique=True, editable=False)


    class Meta:
        # Add constraints to prevent similar establishments
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'owner', 'region'],
                name='unique_establishment_per_owner_region'
            )
        ]

    def clean(self):
        from django.core.exceptions import ValidationError
        
        # Convert name to lowercase for case-insensitive comparison
        name_lower = self.name.lower()
        
        # Check for similar establishments
        similar_establishments = Establishment.objects.filter(
            name__iexact=self.name,
            type=self.type,
            region=self.region
        ).exclude(pk=self.pk)  # Exclude self when updating

        if similar_establishments.exists():
            raise ValidationError({
                'name': 'An establishment with a similar name already exists in this region.'
            })

    def save(self, *args, **kwargs):
        if not self.establishment_id:
            last_establishment = Establishment.objects.order_by('-id').first()
            if last_establishment:
                last_id = int(last_establishment.establishment_id[3:])
                new_id = f"EST{last_id + 1:06d}"
            else:
                new_id = "EST000001"
            self.establishment_id = new_id
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name} ({self.establishment_id})"