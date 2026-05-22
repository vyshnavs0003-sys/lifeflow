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
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100) 
    password = forms.CharField(widget = forms.PasswordInput)      

