
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', invoice, name="invoice"),
    # path('invoice', invoice, name="invoice"),
    # path('i', invoice, name="invoice"),
    path('gInvoice', generate, name="gInvoice"),
    path('view/<id>', IIView, name="view"),
    path('edit/<id>', IIEdit, name="edit"),
    path('delete/<id>/<action>', IIDelete, name="delete"),
    path("save/<id>/<name>/<phone>/<orders>/<count>/<total>/<aw>/<DD>/<shipping>/<Cur>", IISave, name="IIsave"),
    path("gPDFInvoice/<name>/<phone>/<orders>/<count>/<total>/<aw>/<DD>/<shipping>/<Cur>", genPDFInvoice, name="gPDFInvoice"),
    path("g/<name>/<Cur>/<phone>", genPDFInvoice, name="g"),
    path("ppi/<id>", printPDF, name="ppi")
]