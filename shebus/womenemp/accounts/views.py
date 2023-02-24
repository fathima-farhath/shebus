from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return render(request,'index.html')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'login.html')
    return render(request,'login.html')
    

def reg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.add_message(request, messages.INFO, f'Welcome {user.get_full_name()}!!!Your account has been registered successfully.')
            return render(request,'home.html')
    else:
        form = SignUpForm()
    return render(request,'reg.html',{'form':form})
