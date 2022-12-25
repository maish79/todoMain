from django import forms
from django.forms import ModelForm

from .models import *

class listForm(forms.ModelForm):

    class Meta:
        model = list
        fields = '__all__'