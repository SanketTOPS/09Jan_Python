from django.contrib import admin
from .models import *

# Register your models here.
class studinfoData(admin.ModelAdmin):
    list_display=['name','email','city']

admin.site.register(studinfo,studinfoData)
