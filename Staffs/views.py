from django.shortcuts import render, redirect
from .models import BioData, Agreement, Guarantor
from .forms import *
from django.http import HttpResponse
# Create your views here.

def AddStaffsBioDataform(request):
  BDform = BioDataform(request.POST)
  Gform = Guarantorform(request.POST)
  Aform = Agreementform(request.POST)
  if request.method == "POST":
    Aform = Agreementform(data=request.POST, files=request.FILES)
    if BDform.is_valid() and Gform.is_valid() and Aform.is_valid():
      BDform.save()
      Aform.save()
      Gform.save()
      return redirect('/')
  else:
    BDform = BioDataform(request.POST)
    Gform = Guarantorform(request.POST)
    Aform = Agreementform(request.POST)
  return render(request, 'Staffs/addstaffsBioDataform.html',{
       "bioDataform":BDform,
       "guarantorform":Gform,
       "agreementform":Aform,
    })

def AddStaffsPassport(request):
  BDform = BioDataform(request.POST)
  Gform = Guarantorform(request.POST)
  Aform = Agreementform(request.POST)
  if request.method == "POST":
    if BDform.is_valid() and Gform.is_valid() and Aform.is_valid():
      BDform.save()
      Gform.save()
      Aform.save()
      return redirect('/')
  else:
    BDform = BioDataform(request.POST)
    Gform = Guarantorform(request.POST)
    Aform = Agreementform(request.POST)
  return render(request, 'Staffs/addstaffsBioDataform.html',{
       "bioDataform":BDform,
       "guarantorform":Gform,
      "agreementform":Aform,
    })


def StaffsIndex(request):
    bioData = BioData.objects.all().order_by("-id")
    return render(request, 'Staffs/staffsIndex.html', {
       "BioData":bioData
    })


def Staffs(request):
    bioData = BioData.objects.get(id = id)
    agreement = Agreement.objects.get(id = id)
    guarantor = Guarantor.objects.get(id = id)
    return render(request, 'Staffs/staffs.html')


def UpdateStaffs(request):
  bioData = BioData.objects.get(id =id)
  agreement = Agreement.objects.get(id = id)
  guarantor = Guarantor.objects.get(id = id)
  
  if request.method == "POST":
    bioDataForm = BioDataform()
    if bioDataForm.is_valid():
      bioData.Surname = bioDataForm.cleaned_data.get('Surname')
      bioData.Firstname = bioDataForm.cleaned_data.get('Firstname')
      bioData.Other = bioDataForm.cleaned_data.get('Other')
      bioData.Sex = bioDataForm.cleaned_data.get('Sex')
      bioData.Date_of_Birth = bioDataForm.cleaned_data.get('Date_of_Birth')
      bioData.State_of_Origin = bioDataForm.cleaned_data.get('State_of_Origin')
      bioData.LGA = bioDataForm.cleaned_data.get('LGA')
      bioData.Marital_Status = bioDataForm.cleaned_data.get('Marital_Status')
      bioData.Religion = bioDataForm.cleaned_data.get('Religion')
      bioData.Home_Address = bioDataForm.cleaned_data.get('Home_Address')
      bioData.Phone_Number = bioDataForm.cleaned_data.get('Phone_Number')
      bioData.Next_Of_Kin = bioDataForm.cleaned_data.get('Next_Of_Kin')
      bioData.Relationship = bioDataForm.cleaned_data.get('Relationship')
      bioData.NOK_Phone = bioDataForm.cleaned_data.get('NOK_Phone')
      bioData.Email_Adress = bioDataForm.cleaned_data.get('Email_Adress')
      bioData.save()
  
  if request.method == "POST":
    aForm = Agreementform(data=request.POST, files=request.FILES)
    if aForm.is_valid():
      agreement.Name = aForm.cleaned_data.get('Name')
      agreement.Passport = aForm.cleaned_data.get("Passport")
      agreement.Working_Hours = aForm.cleaned_data.get('Working_Hours')
      agreement.Break_Time = aForm.cleaned_data.get('Break_Time')
      agreement.Closing_Hours = aForm.cleaned_data.get('Closing_Hours')
      agreement.To_Produce = aForm.cleaned_data.get('To_Produce')
      agreement.Salary = aForm.cleaned_data.get('Salary')
      agreement.Work_Duration = aForm.cleaned_data.get('Work_Duration')
      agreement.Terms_And_Conditions = aForm.cleaned_data.get('Terms_And_Conditions')
      agreement.save()
  
  if request.method == "POST":
    gForm = Guarantorform(data=request.POST, files=request.FILES)
    if gForm.is_valid():
      guarantor.Surname = gForm.cleaned_data.get('Client_Name')
      guarantor.Firstname = gForm.cleaned_data.get('Firstname')
      guarantor.Other = gForm.cleaned_data.get('Other')
      guarantor.Sex = gForm.cleaned_data.get('Sex')
      guarantor.Date_of_Birth = gForm.cleaned_data.get('Date_of_Birth')
      guarantor.State_of_Origin = gForm.cleaned_data.get('State_of_Origin')
      guarantor.LGA = gForm.cleaned_data.get('LGA')
      guarantor.Marital_Status = gForm.cleaned_data.get('Marital_Status')
      guarantor.Religion = gForm.cleaned_data.get('Religion')
      guarantor.Home_Address = gForm.cleaned_data.get('Home_Address')
      guarantor.Phone_Number = gForm.cleaned_data.get('Phone_Number')
      guarantor.Next_Of_Kin = gForm.cleaned_data.get('Next_Of_Kin')
      guarantor.Relationship = gForm.cleaned_data.get('Relationship')
      guarantor.NOK_Phone = gForm.cleaned_data.get('NOK_Phone')
      guarantor.Email_Adress = gForm.cleaned_data.get('Email_Adress')
      guarantor.save()
    return render(request, 'Staffs/updatestaffs.html')


def RemoveStaffs(request, id, action):
    bioData = BioData.objects.get(id = id)
    agreement = Agreement.objects.get(id = id)
    guarantor = Guarantor.objects.get(id = id)
    
    if action == "YES":
        bioData.delete()
        agreement.delete()
        guarantor.delete()
        return redirect('/staffs')

    # return render(request, "Invoice/delete.html", {"ID":id, "invoice":Invoice.objects.get(id=id)})
    return render(request, 'Staffs/delete.html', {"bioData":bioData})

def ViewStaff(request, id):
  BD = BioData.objects.get(id = id)
  G = Guarantor.objects.get(id = id)
  A = Agreement.objects.get(id = id)
  return render(request, 'Staffs/view.html', {"BioData":BD, "Guarantor":G, "Agreement":A})