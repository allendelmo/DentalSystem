from django.db import models

# Create your models here.
class Patient(models.Model):
    # id (should be auto generated)
    first_name = models.CharField()
    last_name = models.CharField()
    date_of_birth = models.DateTimeField()
    gender = models.CharField()
    address = models.CharField()
    phone = models.CharField()
    email = models.CharField()
    emergency_contact = models.CharField()

    def __str__(self):
        return self.email 
