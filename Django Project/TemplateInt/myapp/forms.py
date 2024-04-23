from django import forms
from .models import *

class contactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'