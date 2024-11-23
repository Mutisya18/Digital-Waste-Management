from django.shortcuts import render, redirect
#from django.urls import reverse  # Import this
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .forms import EstablishmentForm
from .models import Establishment
from django.http import JsonResponse
from .models import Region
from django.shortcuts import get_object_or_404


def get_regions(request):
    q = request.GET.get('q', '')
    regions = Region.objects.filter(name__icontains=q)[:10]
    return JsonResponse({'regions': list(regions.values('id', 'name'))})
    
@login_required
def register_establishment(request):
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            try:
                establishment = form.save(commit=False)
                establishment.owner = request.user
                establishment.save()
                messages.success(request, "You have successfully registered and establishment")
                return redirect('establishment_success', establishment_id=establishment.id)
            except IntegrityError:
                messages.error(request, "An establishment with this Plus Code already exists. You can't register it again.")
    else:
        form = EstablishmentForm(user=request.user)
    return render(request, 'establishment_registration/register.html', {'form': form})

@login_required
def establishment_success(request, establishment_id):
    establishment = Establishment.objects.get(id=establishment_id)
    owner = establishment.owner
    return render(request, 'establishment_registration/success.html', {
        'establishment': establishment,
        'owner': owner,
    })

def get_establishments_by_region(request):
    region_id = request.GET.get('region_id')
    if region_id:
        establishments = Establishment.objects.filter(region_id=region_id).values('id', 'name')
        return JsonResponse({'establishments': list(establishments)})
    return JsonResponse({'establishments': []})


@login_required
def edit_establishment(request, establishment_id):
    establishment = get_object_or_404(Establishment, id=establishment_id, owner=request.user)
    if request.method == 'POST':
        form = EstablishmentForm(request.POST, instance=establishment)
        if form.is_valid():
            form.save()
            messages.success(request, "Establishment details updated successfully.")
            return redirect('owner_dashboard')
    else:
        form = EstablishmentForm(instance=establishment)
    return render(request, 'establishment_registration/edit_establishment.html', {'form': form, 'establishment': establishment})

@login_required
def delete_establishment(request, establishment_id):
    establishment = get_object_or_404(Establishment, id=establishment_id, owner=request.user)
    establishment.delete()
    messages.success(request, "Establishment deleted successfully.")
    return redirect('owner_dashboard')
