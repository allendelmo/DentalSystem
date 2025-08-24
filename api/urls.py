from django.urls import path
from . import views

urlpatterns = [
    path("patients/", views.PatientListCreate.as_view(), name="patient-view-create")
]