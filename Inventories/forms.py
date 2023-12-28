from .models import *
from django import forms
from .models import Items
from django.forms.widgets import DateInput

class Itemsform(forms.ModelForm):
    update_Date = forms.DateField(required=True,widget=DateInput(attrs={'class':'form-control', 'placeholder':'Date','type': 'date'}))
    class Meta:
        model = Items
        fields = ("__all__")