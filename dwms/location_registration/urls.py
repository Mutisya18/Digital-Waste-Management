from django.urls import path
from . import views

urlpatterns = [
    path('establishments/', views.establishment_list, name='establishment_list'),
    path('establishment/<int:pk>/', views.establishment_detail, name='establishment_detail'),
    path('establishment/create/', views.create_establishment, name='create_establishment'),
    path('locations/', views.location_list, name='location_list'),
    path('location/<int:pk>/', views.location_detail, name='location_detail'),
    path('location/create/', views.create_location, name='create_location'),
]
