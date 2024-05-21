from django.contrib import admin
from django.urls import path,include
from myap import views

urlpatterns = [
    path('',views.index),
]