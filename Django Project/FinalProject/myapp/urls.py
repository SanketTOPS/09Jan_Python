from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('notes/',views.notes,name='notes'),
    path('profile/',views.profile),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('usersignup/',views.usersignup),
    path('blog/',views.blog),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('userlogout/',views.userlogout),
]