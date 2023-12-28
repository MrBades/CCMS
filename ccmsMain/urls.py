
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'ccmsMain'

urlpatterns = [
    path('main', index, name="main"),
    path('', index, name="main")
]