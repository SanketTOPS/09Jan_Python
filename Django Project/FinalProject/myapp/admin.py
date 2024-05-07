from django.contrib import admin
from .models import *

# Register your models here.
class signupAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','username','city','state','mobile']

class contactAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','phone','email','msg']


class NotesAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','title','opt','myfile','comments']

admin.site.register(signup,signupAdmin)
admin.site.register(contactus,contactAdmin)
admin.site.register(notes,NotesAdmin)
