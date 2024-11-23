from django.urls import path
from . import views

urlpatterns = [
    path('enroll/', views.enroll_occupant, name='enroll_occupant'),
    path('success/', views.enrollment_success, name='enrollment_success'),
    path('get_establishments_by_region/', views.get_establishments_by_region, name='get_establishments_by_region'),
    path('unenroll/<int:enrollment_id>/', views.unenroll_occupant, name='unenroll'),

]