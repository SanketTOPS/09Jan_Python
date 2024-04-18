from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':

        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user: 
            print("Login Successfull!")

            request.session['user']=unm #session create
            request.session.set_expiry(60)
            return redirect('home')
        else:
            print("Error!Login Faild....")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})
    

def userlogout(request):
    logout(request)
    return redirect('/')
