from django.shortcuts import render
from .models import *
from .serialization import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all()
    serial=studSerializer(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=studSerializer(stid)
    return Response(data=serial.data)


@api_view(['GET','DELETE'])
def deleteid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=studSerializer(stid)
        return Response(data=serial.data)
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serail=studSerializer(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=studSerializer(stid)
        return Response(data=serial.data)
    if request.method=='PUT':
        serail=studSerializer(data=request.data,instance=stid)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
