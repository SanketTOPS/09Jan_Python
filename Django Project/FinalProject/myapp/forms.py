from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'


class contactForm(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'