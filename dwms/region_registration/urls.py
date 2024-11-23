# region_registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_region, name='register_region'),
    # Add other URLs as needed
        path('list/', views.region_list, name='region_list'),
]
