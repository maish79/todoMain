from django import forms
from django.forms import ModelForm

from .models import *

class listForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new list...'}))

    class Meta:
        model = list
        fields = '__all__'