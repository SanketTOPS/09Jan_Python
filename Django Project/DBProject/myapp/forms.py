from django import forms
from .models import *


class userForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'