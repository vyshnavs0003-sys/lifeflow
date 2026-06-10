from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Donor, BloodRequest, Hospital, BloodInventory


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['blood_group','age','location','medical_issues','last_donation_date', 'available_for_donation','consent_to_contact']

        widgets = {
            'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_issues': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'last_donation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'available_for_donation': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'consent_to_contact': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class BloodRequestForm(forms.ModelForm):

    class Meta:
        model = BloodRequest
        fields = ['patient_name','patient_id','blood_group_needed','units_needed','hospital','reason','required_date','contact_number']

        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_id': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_group_needed': forms.TextInput(attrs={'class': 'form-control'}),
            'units_needed': forms.NumberInput(attrs={'class': 'form-control'}),
            'hospital': forms.Select(attrs={'class': 'form-select'}),
            'reason': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'required_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name', 'location', 'contact']

        widgets = {
            'hospital_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BloodInventoryForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_group', 'units_available']

        widgets = {
            'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
            'units_available': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone','password1','password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))