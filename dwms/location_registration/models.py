from django.db import models

class EstablishmentType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Establishment(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(EstablishmentType, on_delete=models.CASCADE)
    main_plus_code = models.CharField(max_length=20, unique=True)
    total_stories = models.PositiveIntegerField(null=True, blank=True)
    owner_name = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=255)
    plus_code = models.CharField(max_length=20, unique=True)
    floor = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.establishment.name}"
