from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        newdata=userForm(request.POST)
        if newdata.is_valid():
            newdata.save()
            print("Your data has been saved!")
        else:
            print(newdata.errors)
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})


def deletedata(request,id):
    userid=userinfo.objects.get(id=id)
    userinfo.delete(userid)
    return redirect('showdata')

def updatedata(request,id):
    userid=userinfo.objects.get(id=id)
    if request.method=='POST':
        update=userForm(request.POST,instance=userid)
        if update.is_valid():
            update.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(update.errors)
    return render(request,'updatedata.html',{'userid':userid})