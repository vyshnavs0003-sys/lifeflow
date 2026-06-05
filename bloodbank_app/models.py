from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    medical_issues = models.TextField(blank=True)
    last_donation_date = models.DateField(null=True, blank=True)
    available_for_donation = models.BooleanField(default=True)
    consent_to_contact = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
class Hospital(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.hospital_name

class BloodInventory(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10)
    units_available = models.IntegerField()

    def __str__(self):
        return f"{self.hospital.hospital_name} - {self.blood_group}"

class BloodRequest(models.Model):
    requested_by = models.ForeignKey(User,on_delete=models.CASCADE)  
    patient_name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=50)
    blood_group_needed= models.CharField(max_length=10)
    units_needed= models.IntegerField()
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    reason = models.TextField()
    required_date = models.DateField()
    contact_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20,default='Pending')

    def __str__(self):
        return self.patient_name

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('USER','User'),
        ('HOSPITAL','Hospital')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='USER')
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.role}"