from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        newcontact=contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been saved!")
        else:
            print(newcontact.errors)
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')