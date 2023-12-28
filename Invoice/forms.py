
from django import forms
from .models import Invoice
from django.forms.widgets import DateInput

class Invoiceform(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ("__all__")