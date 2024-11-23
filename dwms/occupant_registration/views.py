from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OccupantEnrollmentForm
from .models import Occupant, Establishment
from django.http import JsonResponse
from .models import Establishment
from .models import Occupant
from django.shortcuts import redirect, get_object_or_404


@login_required
def enroll_occupant(request):
    if request.method == 'POST':
        form = OccupantEnrollmentForm(request.POST)
        if form.is_valid():
            occupant = form.save(commit=False)
            occupant.occupant = request.user
            occupant.save()
            messages.success(request, "You have been successfully enrolled!")
            return redirect('enrollment_success')
    else:
        form = OccupantEnrollmentForm()
    return render(request, 'occupant_registration/enroll.html', {'form': form})

def get_establishments_by_region(request):
    region_id = request.GET.get('region_id')
    establishments = Establishment.objects.filter(region_id=region_id).values('id', 'name')
    return JsonResponse({'establishments': list(establishments)})
    
@login_required
def enrollment_success(request):
    return render(request, 'occupant_registration/success.html')

@login_required
def unenroll_occupant(request, enrollment_id):
    # Get the enrollment object and delete it if the user is the occupant
    enrollment = get_object_or_404(Occupant, id=enrollment_id, occupant=request.user)
    enrollment.delete()
    messages.success(request, "You have been successfully unenrolled from the establishment.")
    return redirect('occupant_dashboard')