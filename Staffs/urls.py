
from django.contrib import admin
from django.urls import path
from .views import StaffsIndex, AddStaffsBioDataform, RemoveStaffs, UpdateStaffs, ViewStaff

urlpatterns = [
    path('', StaffsIndex, name='SIndex'),
    path('SIndex', StaffsIndex, name='SIndex'),
    path('newStaff', AddStaffsBioDataform, name="newStaff"),
    path('view/<id>', ViewStaff, name="view"),
    path('edit/<id>', UpdateStaffs, name="edit"),
    path('delete/<id>/<action>', RemoveStaffs, name="delete"),
]