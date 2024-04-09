from django.contrib import admin
from .models import *

# Register your models here.

class userdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','email','mobile','dob']

admin.site.register(userinfo,userdata)