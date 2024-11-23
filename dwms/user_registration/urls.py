from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('homepage/', views.homepage_view, name='homepage'),
    path('choose-role/', views.choose_role, name='choose_role'),
    path('dashboard/occupant/', views.occupant_dashboard, name='occupant_dashboard'),
    path('dashboard/owner/', views.owner_dashboard, name='owner_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
#    path('become-occupant/', views.become_occupant, name='become_occupant'),
#    path('become-owner/', views.become_owner, name='become_owner'),
    path('register_as_owner/', views.register_as_owner, name='register_as_owner'),
    path('register_as_occupant/', views.register_as_occupant, name='register_as_occupant'),
    path('set_active_role/<str:role>/', views.set_active_role, name='set_active_role'),
    path('switch-role/', views.switch_role, name='switch_role'),


]