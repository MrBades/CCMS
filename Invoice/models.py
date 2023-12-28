from django.db import models
from datetime import date, timedelta

# Create your models here.
class CUR(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name
    
def defCurency():
        return "USD"
    
class Invoice(models.Model):
    Customer_Name = models.CharField(max_length=1000, null=True, default='non')
    Order_Date = models.DateField(default=date.today())
    Due_Date = models.CharField(max_length=1000, null=True, default='non')
    Phone = models.CharField(max_length=1000, null=True, default='non')
    AW = models.CharField(max_length=1000, null=True, default='non')
    Orders = models.CharField(max_length=1000, null=True, default='non')
    Count = models.CharField(max_length=1000, null=True, default='non')
    Curency = models.ForeignKey(CUR, on_delete=models.SET_NULL, null=True, default=defCurency())
    Amount = models.CharField(max_length=1000)
    Shipping = models.CharField(max_length=1000)
    Subtotal = models.CharField(max_length=100, null=True, default='non')
    NameId = models.CharField(max_length=1000, null=True, default='non')
    VAT = models.CharField(max_length=1000, null=True, default='non')
    Total = models.CharField(max_length=1000, null=True, default='non')


class Bank_Details(models.Model):
    Name = models.CharField(max_length=10000)
    Account_Number = models.CharField(max_length=10000)
    Bank = models.CharField(max_length=1000)
    Swift_Code = models.CharField(max_length=1000)
    Mail = models.CharField(max_length=10000)

