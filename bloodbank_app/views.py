from django.shortcuts import render ,redirect

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from .models import UserProfile,Hospital,BloodInventory
from .forms import RegisterForm,LoginForm,BloodInventoryForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(  user = user)
            return redirect ('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form})         

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username=username,
                password=password
            ) 
            if user is not None:
                login(request, user)
                profile = UserProfile.objects.get(
                    user = request.user
                )
                if profile.role == 'HOSPITAL':
                    return redirect(
                        'hospital_dashboard'
                    )
                else:
                    return redirect(
                        'user_dashboard'
                    )
            else:
                return render(request,'login.html',{'form':form,'error':'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})    

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_dashboard(request):
    return render(request,'user_dashboard.html')

@login_required
def hospital_dashboard(request):
    hospital = Hospital.objects.get(user = request.user)
    inventories = BloodInventory.objects.filter(hospital = hospital)
    return render(request,'hospital_dashboard.html',{'hospital': hospital,'inventories': inventories})

@login_required
def add_inventory(request):
    hospital = Hospital.objects.get(user = request.user)
    if request.method == 'POST':
        form = BloodInventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.hospital = hospital
            inventory.save()
            return redirect('hospital_dashboard')
    else:
        form = BloodInventoryForm()
        return render(request,'add_inventory.html',{'form': form})    

