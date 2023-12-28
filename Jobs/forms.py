from .models import *
from django import forms
from django.forms.widgets import FileInput
from django.forms.widgets import TextInput, FileInput, DateInput, Textarea, DateTimeInput, EmailInput

class Jobsform(forms.ModelForm):
    Date = forms.DateField(required=True,widget=DateInput(attrs={'class':'form-control', 'placeholder':'Date','type': 'date'}))
    Delivery_Date = forms.DateField(required=True,widget=DateInput(attrs={'class':'form-control', 'placeholder':'Delivery Date','type': 'date'}))
    class Meta:
        model = Jobs
        fields = ("__all__")

class JobsEditform(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ("__all__")