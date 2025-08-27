from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

        # # if we want to select only specific fields, use the array below
        # fields = [
        #     "id",
        #     "first_name",
        #     "last_name",
        #     "date_of_birth",
        #     "gender",
        #     "address",
        #     "phone",
        #     "email",
        #     "emergency_contact",
        # ]
