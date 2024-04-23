from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    service=models.CharField(max_length=100)
    email=models.EmailField()
    msg=models.TextField()