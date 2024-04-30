from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'