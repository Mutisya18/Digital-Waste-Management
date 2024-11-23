from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.backends import ModelBackend
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
#from .forms import ProfileEditForm 
from occupant_registration.models import Occupant
from establishment_registration.models import Establishment  # Import Establishment model
from occupant_registration.forms import OccupantEnrollmentForm  # Import form for Occupant
from establishment_registration.forms import EstablishmentForm  # Import form for Owner

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RoleSwitchForm


def redirect_to_login(request):
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # After saving, you should redirect to a success page or login page
            return redirect('login')  # or 'homepage' depending on your setup
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_registration/register.html', {'form': form})

    
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
             # Check if user has already chosen their initial role
            if not user.has_chosen_initial_role:
                return redirect('choose_role')
            
            # Direct to appropriate dashboard based on current role
            if user.current_role == 'owner':
                return redirect('owner_dashboard')
            else:
                return redirect('occupant_dashboard')
    
            # Set the current role in session
            if not request.session.get('user_role'):
                request.session['user_role'] = user.current_role or (
                    'owner' if user.is_owner else 'occupant'
                )
            return redirect('homepage')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user_registration/login.html', {'form': form})

@login_required
def homepage_view(request):
    """Redirect user based on the active role stored in the session."""
    active_role = request.session.get('active_role')
    if active_role == 'occupant' and request.user.is_occupant:
        return redirect('occupant_dashboard')
    elif active_role == 'owner' and request.user.is_owner:
        return redirect('owner_dashboard')
    else:
        return redirect('choose_role')  # If no active role, prompt user to choose

@login_required
def occupant_dashboard(request):
    if not request.user.is_occupant:
        return redirect('owner_dashboard')  # Redirect if the user is not an occupant
     # Get user’s enrollments
    enrollments = Occupant.objects.filter(occupant=request.user)
    context = {
        'user': request.user,
        'enrollments': enrollments,
    }
    return render(request, 'user_registration/occupant_dashboard.html', context)



#chatgpt
@login_required
def choose_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'occupant':
            request.user.is_occupant = True
            request.user.is_owner = False
            redirect_url = 'occupant_dashboard'
        elif role == 'owner':
            request.user.is_owner = True
            request.user.is_occupant = False
            redirect_url = 'owner_dashboard'
        else:
            # If no valid role is selected, re-render the role selection page
            return render(request, 'user_registration/choose_role.html', {'error': 'Please select a valid role.'})
        
        # Save the user after updating the role and redirect to the chosen dashboard
        request.user.save()
        return redirect(redirect_url)

    # Render the role selection page if the request method is GET
    return render(request, 'user_registration/choose_role.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('occupant_dashboard' if request.user.is_occupant else 'owner_dashboard')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'user_registration/edit_profile.html', {'form': form})

@login_required
def owner_dashboard(request):
    owned_establishments = Establishment.objects.filter(owner=request.user)
    establishments_with_occupants = []

    for establishment in owned_establishments:
        occupants = Occupant.objects.filter(establishment=establishment)
        establishments_with_occupants.append({
            'establishment': establishment,
            'occupants': occupants,
        })

    context = {
        'user': request.user,
        'establishments_with_occupants': establishments_with_occupants,
    }
    return render(request, 'user_registration/owner_dashboard.html', context)

@login_required
def become_occupant(request):
    # Toggle the user to also be an occupant if they aren’t already
    if not request.user.is_occupant:
        request.user.is_occupant = True
        request.user.save()
    return redirect('occupant_dashboard')  # Redirect to occupant dashboard

@login_required
def become_owner(request):
    # Toggle the user to also be an owner if they aren’t already
    if not request.user.is_owner:
        request.user.is_owner = True
        request.user.save()
    return redirect('owner_dashboard')  # Redirect to owner dashboard


@login_required
def register_as_occupant(request):
    """Page to register as an occupant if the user isn’t one already."""
    if request.method == 'POST':
        form = OccupantEnrollmentForm(request.POST)
        if form.is_valid():
            occupant = form.save(commit=False)
            occupant.occupant = request.user
            occupant.save()
            request.user.is_occupant = True
            request.user.save()
            return redirect('occupant_dashboard')
    else:
        form = OccupantEnrollmentForm()
    return render(request, 'occupant_registration/enroll.html', {'form': form})

@login_required
def register_as_owner(request):
    """Page to register as an owner if the user isn’t one already."""
    if request.method == 'POST':
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            establishment = form.save(commit=False)
            establishment.owner = request.user
            establishment.save()
            request.user.is_owner = True
            request.user.save()
            return redirect('owner_dashboard')
    else:
        form = EstablishmentForm()
    return render(request, 'establishment_registration/register.html', {'form': form})


@login_required
def set_active_role(request, role):
    """Set the active role for the user."""
    if role == 'occupant' and request.user.is_occupant:
        request.session['active_role'] = 'occupant'
        return redirect('occupant_dashboard')
    elif role == 'owner' and request.user.is_owner:
        request.session['active_role'] = 'owner'
        return redirect('owner_dashboard')
    else:
        return redirect('choose_role')  # Redirect to role selection if role is invalid

@login_required
def switch_role(request):
    current_role = request.session.get('user_role', request.user.current_role)
    target_role = 'owner' if current_role == 'occupant' else 'occupant'
    
    if request.method == 'POST':
        if 'switch_role' in request.POST:
            # Just switching between existing roles
            request.user.current_role = target_role
            request.user.save()
            request.session['user_role'] = target_role
            return redirect('homepage')
            
        form = RoleSwitchForm(request.POST)
        if form.is_valid():
            if target_role == 'owner':
                request.user.is_owner = True
            else:
                request.user.is_occupant = True
            
            request.user.current_role = target_role
            request.user.save()
            request.session['user_role'] = target_role
            return redirect('homepage')
    else:
        form = RoleSwitchForm()
    
    return render(request, 'user_registration/switch_role.html', {
        'form': form,
        'target_role': target_role
    })

@login_required
def choose_role(request):
    if request.user.has_chosen_initial_role:
        # If user has already chosen role, redirect to appropriate dashboard
        if request.user.current_role == 'owner':
            return redirect('owner_dashboard')
        return redirect('occupant_dashboard')
    
    if request.method == 'POST':
        role = request.POST.get('role')
        if role in ['owner', 'occupant']:
            request.user.current_role = role
            if role == 'owner':
                request.user.is_owner = True
            else:
                request.user.is_occupant = True
            request.user.has_chosen_initial_role = True
            request.user.save()
            
            request.session['user_role'] = role
            return redirect(f'{role}_dashboard')
    
    return render(request, 'user_registration/choose_role.html')