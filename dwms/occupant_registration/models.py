from django.db import models

# Create your models here.
from django.db import models
from user_registration.models import CustomUser
from establishment_registration.models import Establishment


class Occupant(models.Model):
    OCCUPANT_TYPE = [
        ('OFFICE', 'Office'),
        ('APARTMENT', 'Rental'),
        ('CHURCH', 'Church'),
        ('SCHOOL', 'School'),
        ('HOME', 'Home'),
        ('BUSINESS', 'Business'),
        ('OTHER', 'Other'),
    ]
    
    occupant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    floor_number = models.IntegerField(null=True, blank=True)
    plus_code = models.CharField(max_length=20, unique=True)
    occupancy_type = models.CharField(max_length=20, choices=OCCUPANT_TYPE)  # e.g., Tenant, Business, etc.
    related_name='occupants'  # Add this line

    def __str__(self):
        return f"{self.occupant.name} enrolled at {self.establishment.name}"