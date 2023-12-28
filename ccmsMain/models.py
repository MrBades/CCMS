from django.db import models
from .validators import file_size

myTo = "sitesIMGS/%y"

# Create your models here.
class Purpose(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name
    
class WebsiteResources(models.Model):
    Admin_Name = models.CharField(max_length=100, default="CarewCouture")
    Name = models.CharField(max_length=100)
    Site_Upload = models.FileField(upload_to=myTo, validators=[file_size], blank=True)
    Purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, null=True)
    Document_Description = models.TextField(max_length=1000000,)

    def __str__(self) :
        return self.Admin_Name + " " + self.Name
    
class Bank_Details(models.Model):
    Name = models.CharField(max_length=10000)
    Account_Number = models.CharField(max_length=10000)
    Bank = models.CharField(max_length=1000)
    Swift_Code = models.CharField(max_length=1000)
    Mail = models.CharField(max_length=10000)
    