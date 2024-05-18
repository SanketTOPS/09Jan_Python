from django.shortcuts import render
import json
import requests

# Create your views here.
def index(request):
    url="https://restcountries.com/v3.1/all"
    req=requests.get(url)
    data=req.json()
    print(data)
    return render(request,'index.html',{'data':data})
