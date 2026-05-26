from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Donor,BloodRequest,Hospital,BloodInventory

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['donor_name','blood_group','phone','location','age','last_donation_date']


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['patient_name','patient_id','blood_group_needed','units_needed','hospital','reason','required_date','contact_number']


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name','location','contact']

class BloodInventoryForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['hospital','blood_group','units_available']   

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100) 
    password = forms.CharField(widget = forms.PasswordInput)          

class BloodInventoryForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_group','units_available']