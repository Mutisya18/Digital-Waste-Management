# Generated by Django 5.1.3 on 2024-11-12 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establishment_registration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_number', models.IntegerField(blank=True, null=True)),
                ('plus_code', models.CharField(max_length=20, unique=True)),
                ('occupancy_type', models.CharField(choices=[('OFFICE', 'Office'), ('APARTMENT', 'Rental'), ('CHURCH', 'Church'), ('SCHOOL', 'School'), ('HOME', 'Home'), ('BUSINESS', 'Business'), ('OTHER', 'Other')], max_length=20)),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establishment_registration.establishment')),
                ('occupant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
