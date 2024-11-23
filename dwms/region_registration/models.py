from django.db import models

# Create your models here.
# region_registration/models.py
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    overall_area = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
