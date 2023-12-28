from django.db import models
from .validators import file_size
from datetime import date, timedelta
from django.utils.translation  import gettext_lazy as _
# Create your models here.
        
myTo = "Passports/%y"

class MaSt(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name

class SEX(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name

class ROLE(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) :
        return self.name
    

def deliveryDay():
    return date.today() + timedelta(days=20)

class BioData(models.Model):  
    Surname = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Other = models.CharField(max_length=100, blank=True, )
    Sex = models.ForeignKey(SEX, on_delete=models.SET_NULL, null=True)
    Date_of_Birth = models.DateField(default=date.today())
    State_of_Origin = models.CharField(max_length=1000, )
    LGA = models.CharField(max_length=100,)
    Marital_Status = models.ForeignKey(MaSt, on_delete=models.SET_NULL, null=True)
    Religion = models.CharField(max_length=1000,)
    Home_Address = models.CharField(max_length=1000,)
    Phone_Number = models.CharField(max_length=1000,)
    Next_Of_Kin = models.CharField(max_length=1000,)
    Relationship = models.CharField(max_length=1000,)
    NOK_Phone = models.CharField(max_length=1000,)
    Email_Adress = models.CharField(max_length=1000,)

    def __str__(self) :
        return self.Surname + " " + self.Firstname
    
class Agreement(models.Model):  
    Name = models.CharField(max_length=100)
    Passport = models.FileField(upload_to=myTo, validators=[file_size], blank=True)
    Date = models.DateField(default=date.today())
    Job_Role = models.ForeignKey(ROLE, on_delete=models.SET_NULL, null=True)
    Working_Hours = models.CharField(max_length=100)
    Break_Time = models.CharField(max_length=100)
    Closing_Hours = models.CharField(max_length=100)
    To_Produce = models.CharField(max_length=100)
    Salary = models.CharField(max_length=1000,)
    Work_Duration = models.CharField(max_length=100,)
    Terms_And_Conditions = models.BooleanField()

    def __str__(self) :
        return self.Name

class Guarantor(models.Model):  
    Surname = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Other = models.CharField(max_length=100, blank=True)
    Sex = models.ForeignKey(SEX, on_delete=models.SET_NULL, null=True)
    Date_of_Birth = models.DateField(default=date.today())
    State_of_Origin = models.CharField(max_length=1000,)
    LGA = models.CharField(max_length=100,)
    Marital_Status = models.ForeignKey(MaSt, on_delete=models.SET_NULL, null=True)
    Religion = models.CharField(max_length=1000,)
    Home_Address = models.CharField(max_length=1000,)
    Phone_Number = models.CharField(max_length=1000,)
    Next_Of_Kin = models.CharField(max_length=1000,)
    Relationship = models.CharField(max_length=1000,)
    NOK_Phone = models.CharField(max_length=1000,)
    NOK_Email_Adress = models.CharField(max_length=1000,)

    def __str__(self):
        return self.Surname + " " + self.Firstname
    