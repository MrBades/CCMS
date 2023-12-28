from django.contrib import admin
from .models import Jobs
# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    list_display = ("id", "Client_Name", "Date", "Delivery_Date")
admin.site.register(Jobs, JobsAdmin)

