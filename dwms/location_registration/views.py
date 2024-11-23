from django.shortcuts import render, redirect, get_object_or_404
from .models import Establishment, Location, EstablishmentType
from .forms import EstablishmentForm, LocationForm
from django.contrib.auth.decorators import login_required

@login_required
def establishment_list(request):
    establishments = Establishment.objects.all()
    return render(request, 'location_registration/establishment_list.html', {'establishments': establishments})

@login_required
def establishment_detail(request, pk):
    establishment = get_object_or_404(Establishment, pk=pk)
    locations = establishment.locations.all()
    return render(request, 'location_registration/establishment_detail.html', {'establishment': establishment, 'locations': locations})

@login_required
def create_establishment(request):
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('establishment_list')
    else:
        form = EstablishmentForm()
    return render(request, 'location_registration/create_establishment.html', {'form': form})

@login_required
def create_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'location_registration/create_location.html', {'form': form})

@login_required
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location_registration/location_list.html', {'locations': locations})

@login_required
def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, 'location_registration/location_detail.html', {'location': location})
