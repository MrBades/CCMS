from django.db import models
from datetime import date
from django.utils.timezone import now
from django.utils import dates
from django.utils.translation  import gettext_lazy as _
# Create your models here.

class Colors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

    def  object(self):
        return self.name.sort()
    
class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Items(models.Model):
    admin_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=1000)
    color = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True,)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    update_Date = models.DateField(default=date.today(), null=True)

    def __str__(self) :
        return self.admin_name