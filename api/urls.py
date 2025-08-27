from django.urls import path
from . import views

urlpatterns = [
    path("patients/", views.PatientListCreate.as_view(), name="patient-view-create"),
    path("patients/<int:pk>/", views.PatientRetrieveUpdateDestroy.as_view(), name="patient-view-retrieve-update-destroy")
]