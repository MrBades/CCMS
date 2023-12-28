from django.db import models
from .validators import file_size
from datetime import date, timedelta
from django.utils.translation  import gettext_lazy as _
# Create your models here.

def deliveryDay():
    return date.today() + timedelta(days=20)

class Jobs(models.Model):  
    Client_Name = models.CharField(max_length=100)
    Date = models.DateField(default=date.today())
    Delivery_Date = models.DateField(max_length=150, default=deliveryDay,)
    Material = models.FileField(upload_to="designs/%y", validators=[file_size], blank=True) 
    Design = models.FileField(upload_to="designs/%y", validators=[file_size], blank=True) 
    # ____________________----------________________
    Shoulder_to_nipple_point = models.CharField(max_length=100, default='0')
    Shoulder_to_under_burst = models.CharField(max_length=100, default='0')
    Shoulder_to_half_length = models.CharField(max_length=100, default='0')
    Shoulder_to_hip_part = models.CharField(max_length=100, default='0')
    Shoulder_to_knee_length = models.CharField(max_length=100, default='0')
    Shoulder_to_dress_length = models.CharField(max_length=100, default='0')
    Burst = models.CharField(max_length=100, default='0')
    Upper_burst = models.CharField(max_length=100, default='0')
    Under_Burst = models.CharField(max_length=100, default='0')
    High_waist_measurement = models.CharField(max_length=100, default='0')
    Waist_measurement = models.CharField(max_length=100, default='0')
    High_hip = models.CharField(max_length=100, default='0')
    Hip = models.CharField(max_length=100, default='0')
    Knee_measurement = models.CharField(max_length=100, default='0')
    Cleavage_level = models.CharField(max_length=100, default='0')
    Shoulder_measurement = models.CharField(max_length=100, default='0')
    Sleeve_length = models.CharField(max_length=100, default='0')
    Round_sleeve_length = models.CharField(max_length=100, default='0')
    Waist_to_hip = models.CharField(max_length=100, default='0')
    Waist_to_knee = models.CharField(max_length=100, default='0')
    Waist_to_floor = models.CharField(max_length=100, default='0')
    # __________________________________________
    
    Thigh = models.CharField(max_length=100, default='0')
    Slit = models.CharField(max_length=100, default='0')
    Backless = models.CharField(max_length=100, default='0')
    Round_Knee_For_Pant = models.CharField(max_length=100, default='0')

    def __str__(self) :
        return self.Client_Name