from .models import *
from django import forms
from django.forms.widgets import FileInput
from django.forms.widgets import TextInput, FileInput, DateInput, Textarea, DateTimeInput, EmailInput

class Guarantorform(forms.ModelForm):
    Date_of_Birth = forms.DateField(required=True,widget=DateInput(attrs={'class':'form-control', 'placeholder':'DOB','type': 'date'}))
    class Meta:
        model = Guarantor
        fields = ("__all__")

class BioDataform(forms.ModelForm):
    Date_of_Birth = forms.DateField(required=True,widget=DateInput(attrs={'class':'form-control', 'placeholder':'DOB','type': 'date'}))
    class Meta:
        model = BioData
        fields = ("__all__")

class Agreementform(forms.ModelForm):
    Date = forms.DateField(required=True,widget=DateInput(attrs={'class':'form-control', 'placeholder':'DOB','type': 'date'}))
    class Meta:
        model = Agreement
        fields = ("__all__")