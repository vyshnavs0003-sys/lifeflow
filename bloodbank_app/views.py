from django.shortcuts import render ,redirect

from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm,LoginForm

# Create your views here.

def home(request):
    return render(request,'homet.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect ('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form})         

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            passward = form.cleaned_data['passward']
            user = authenticate(
                request,
                username=username,
                passward=passward
            ) 
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request,'login.html',{'form':form,'error':'Invalid username or password'})
        else:
            form = LoginForm()
        return render(request,'login.html',{'form':form})    

def logout_view(request):
    logout(request)
    return redirect('login')