from django.contrib import admin
from .models import *

# Register your models here.
class adminData(admin.ModelAdmin):
    list_display=['name','email','phone','service','msg']


admin.site.register(contact,adminData)