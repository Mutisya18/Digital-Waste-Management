from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EstablishmentType, Establishment, Location

admin.site.register(EstablishmentType)
admin.site.register(Establishment)
admin.site.register(Location)
