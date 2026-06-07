from django.shortcuts import render ,redirect, get_object_or_404

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from .models import UserProfile,Hospital,BloodInventory,Donor,BloodRequest
from .forms import RegisterForm,LoginForm,BloodInventoryForm,DonorForm,BloodRequestForm

# Create your views here.

def home(request):
    return render(request,'home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data['phone']
            UserProfile.objects.create(user=user,phone=phone)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'register.html', {'form': form})  


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password) 
            if user is not None:
                login(request, user)
                profile = UserProfile.objects.get(user = request.user)
                if profile.role == 'HOSPITAL':
                    return redirect('hospital_dashboard')
                else:
                    return redirect('user_dashboard')
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
    is_donor = Donor.objects.filter(user=request.user).exists()
    return render(request,'user_dashboard.html',{'user': request.user,'is_donor': is_donor})


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


@login_required
def update_inventory(request, inventory_id):
    inventory = BloodInventory.objects.get(id = inventory_id)
    if request.method == 'POST':
        form = BloodInventoryForm(request.POST,instance = inventory)
        if form.is_valid():
            form.save()
            return redirect('hospital_dashboard')
    else:
        form = BloodInventoryForm(instance = inventory)
    return render(request,'update_inventory.html',{'form': form})


@login_required
def delete_inventory(request,inventory_id):
    inventory = BloodInventory.objects.get(id = inventory_id)
    inventory.delete()
    return redirect('hospital_dashboard')


@login_required
def check_availability(request):
    blood_group = request.GET.get('blood_group')
    inventories = BloodInventory.objects.all()
    if blood_group:
        inventories = inventories.filter(blood_group = blood_group)
    return render(request,'check_availability.html',{'inventories': inventories})


@login_required
def become_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()
            return redirect('user_dashboard')
    else:
        form = DonorForm()
    return render(request,'become_donor.html',{'form': form})


@login_required
def donor_profile(request):
    donor = Donor.objects.get(user=request.user)
    return render(request,'donor_profile.html',{'donor': donor})


@login_required
def edit_donor_profile(request):
    donor = get_object_or_404(Donor, user=request.user)
    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_profile')
    else:
        form = DonorForm(instance=donor)
    return render(request, 'edit_donor_profile.html', {'form': form})


@login_required
def donor_list(request):
    blood_group = request.GET.get('blood_group')
    donors = Donor.objects.filter(available_for_donation=True)
    if blood_group:
        donors = donors.filter(blood_group__iexact=blood_group)
    return render(request,'donor_list.html',{'donors': donors})

@login_required
def request_blood(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.requested_by = request.user
            blood_request.save()
            return redirect('user_dashboard')
    else:
        form = BloodRequestForm()
    return render(request,'request_blood.html',{'form': form})

@login_required
def my_blood_requests(request):
    requests = BloodRequest.objects.filter(requested_by=request.user).order_by('-request_date')
    return render(request,'my_blood_requests.html',{'requests': requests})

@login_required
def hospital_blood_requests(request):
    hospital = Hospital.objects.get(user=request.user)
    requests = BloodRequest.objects.filter(hospital=hospital).order_by('-request_date')
    return render(request,'hospital_blood_requests.html',{'requests': requests})

@login_required
def update_request_status(request, request_id, status):
    blood_request = BloodRequest.objects.get(id=request_id)
    if blood_request.hospital.user != request.user:
        return redirect('hospital_dashboard')
    blood_request.status = status
    blood_request.save()
    return redirect('hospital_blood_requests')
