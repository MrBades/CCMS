
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', InventoriesIndex, name="INindex"),
    path('INindex/', InventoriesIndex, name="INindex"),
    path('newInvent/', newInventories, name="newInvent"),
    path('view/<id>', viewInvent, name="view"),
    path('edit/<id>', editInvent, name='edit'),
]