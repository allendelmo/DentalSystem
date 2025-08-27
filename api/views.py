from django.shortcuts import render
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "pk"