from django.shortcuts import render

# Create your views here.

# region_registration/views.py
from django.shortcuts import render, redirect
from .forms import RegionForm
from django.contrib import messages
from django.shortcuts import render
from .models import Region

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region_registration/region_list.html', {'regions': regions})

    
def register_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Region registered successfully.")
            return redirect('region_list')  # Assume you have a region list view
    else:
        form = RegionForm()
    return render(request, 'region_registration/register_region.html', {'form': form})
