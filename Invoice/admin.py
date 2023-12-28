from django.contrib import admin
from .models import CUR, Invoice, Bank_Details
# Register your models here.


admin.site.register(CUR)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "Customer_Name", "Order_Date", "Due_Date", "Phone", "Curency", "Total")
admin.site.register(Invoice, InvoiceAdmin)

class BankAdmin(admin.ModelAdmin):
    list_display = ("Name", "Account_Number", "Bank", "Swift_Code", "Mail")
admin.site.register(Bank_Details, BankAdmin)