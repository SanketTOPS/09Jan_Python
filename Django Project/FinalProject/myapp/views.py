from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
import random
from FinalProject import settings
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cuser=signup.objects.get(id=userid)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

def userlogin(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=signup.objects.filter(username=unm,password=pas)
        userid=signup.objects.get(username=unm)
        print("UserID:",userid.id)
        if user:
            print("Login Successfully!")
            request.session['user']=unm
            request.session['userid']=userid.id
            return redirect('notes')
        else:
            print("Error!Invalid Username or Password")
            msg="Error!Invalid Username or Password"
    return render(request,'userlogin.html',{'msg':msg})

def usersignup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")

            #Email Sending Code
            global otp
            otp=random.randint(1111,9999)
            send_mail(subject="Your OTP",message=f"Hello User!\n\nThanks for registration with us!\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Team\n+91 9724799469 | www.tops-int.com",from_email=settings.EMAIL_HOST_USER,recipient_list=[request.POST['username']])
            return redirect('otpverify')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def userlogout(request):
    logout(request)
    return redirect('/')

def blog(request):
    return render(request,'blog.html')

def otpverify(request):
    global otp
    msg=""
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("Verification Successfully!")
            msg="Verification Successfully!"
            return redirect('userlogin')
        else:
            print("Error!Plz enter valid OTP")
            msg="Error!Plz enter valid OTP"
    return render(request,'otpverify.html',{'msg':msg})