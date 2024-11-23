from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_establishment, name='register_establishment'),
    #Remove this line if it's still in your file:
    #path('success/', views.establishment_success, name='establishment_success'),
    path('success/<int:establishment_id>/', views.establishment_success, name='establishment_success'),
    path('get_regions/', views.get_regions, name='get_regions'),
    path('get_establishments_by_region/', views.get_establishments_by_region, name='get_establishments_by_region'),
    path('edit/<int:establishment_id>/', views.edit_establishment, name='edit_establishment'),
    path('delete/<int:establishment_id>/', views.delete_establishment, name='delete_establishment'),
    
]