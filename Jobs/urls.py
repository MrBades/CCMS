
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', JobsIndex, name='JIndex'),
    path("newJob", NewJob, name="newJob"),
    path('view/<id>', JView, name="view"),
    path('edit/<id>', JEdit, name="edit"),
    path('delete/<id>/<action>', JDelete, name="delete"),
    path('search/<query>', Search, name="search"),
    # path('search/', SearchResultsView.as_view(), name="search"),
    
]