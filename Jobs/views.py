from msilib.schema import ListView
from django.shortcuts import render, redirect
from .forms import Jobsform, JobsEditform
from django.http import HttpResponse
from .models import Jobs
from django.db.models import Q
# Create your views here.

def JobsIndex(request):
  return render(request, 'Jobs/jobsIndex.html', {"Jobs":Jobs.objects.all().order_by("-id")})

def NewJob(request):
  if request.method == "POST":
    JobForm = Jobsform(data=request.POST, files=request.FILES)
    if JobForm.is_valid():
      JobForm.save()
      # return HttpResponse("DONE!..<br><a href='http://127.0.0.1:8000/jobs/'>BACK</a>")
      return redirect("/jobs/newJob")
  else:
    JobForm = Jobsform()
    return render(request, "Jobs/newjobs.html", {"JobForm":JobForm})
  

def JEdit(request, id):
  job = Jobs.objects.get(id =id)
  if request.method == "POST":
    JobForm = JobsEditform(data=request.POST, files=request.FILES)
    if JobForm.is_valid():
      job.Client_Name = JobForm.cleaned_data.get('Client_Name')
      job.Date = JobForm.cleaned_data.get('Date')
      job.Delivery_Date = JobForm.cleaned_data.get('Delivery_Date')
      job.Material = JobForm.cleaned_data.get('Material')
      job.Design = JobForm.cleaned_data.get('Design')
      job.Shoulder_to_nipple_point = JobForm.cleaned_data.get('Shoulder_to_nipple_point')
      job.Shoulder_to_under_burst = JobForm.cleaned_data.get('Shoulder_to_under_burst')
      job.Shoulder_to_half_length = JobForm.cleaned_data.get('Shoulder_to_half_length')
      job.Shoulder_to_hip_part = JobForm.cleaned_data.get('Shoulder_to_hip_part')
      job.Shoulder_to_knee_length = JobForm.cleaned_data.get('Shoulder_to_knee_length')
      job.Shoulder_to_dress_length = JobForm.cleaned_data.get('Shoulder_to_dress_length')
      job.Burst = JobForm.cleaned_data.get('Burst')
      job.Upper_burst = JobForm.cleaned_data.get('Upper_burst')
      job.Under_Burst = JobForm.cleaned_data.get('Under_Burst')
      job.High_waist_measurement = JobForm.cleaned_data.get('High_waist_measurement')
      job.Waist_measurement = JobForm.cleaned_data.get('Waist_measurement')
      job.High_hip = JobForm.cleaned_data.get('High_hip')
      job.Hip = JobForm.cleaned_data.get('Hip')
      job.Knee_measurement = JobForm.cleaned_data.get('Knee_measurement')
      job.Cleavage_level = JobForm.cleaned_data.get('Cleavage_level')
      job.Shoulder_measurement = JobForm.cleaned_data.get('Shoulder_measurement')
      job.Sleeve_length = JobForm.cleaned_data.get('Sleeve_length')
      job.Round_sleeve_length = JobForm.cleaned_data.get('Round_sleeve_length')
      job.Waist_to_hip = JobForm.cleaned_data.get('Waist_to_hip')
      job.Waist_to_knee = JobForm.cleaned_data.get('Waist_to_knee')
      job.Waist_to_floor = JobForm.cleaned_data.get('Waist_to_floor')

      
      job.Round_sleeve_length = JobForm.cleaned_data.get('Round_sleeve_length')
      job.Waist_to_hip = JobForm.cleaned_data.get('Waist_to_hip')
      job.Waist_to_knee = JobForm.cleaned_data.get('Waist_to_knee')
      job.Waist_to_floor = JobForm.cleaned_data.get('Waist_to_floor')
      job.save()
      # return redirect('/jobs')
      return HttpResponse("done")
  else:
    JobForm = JobsEditform()
    return render(request, "Jobs/edit.html", {"JobForm":JobForm, "Job":job})

def JView(request, id:int):
  job = Jobs.objects.get(id =id)
  return render(request, "Jobs/view.html", {"Job":job})

def JDelete(request, id, action):
    if action == "YES":
        job = Jobs.objects.get(id = id)
        job.delete()
        return redirect('/jobs')

    return render(request, "Jobs/delete.html", {"ID":id, "invoice":Jobs.objects.get(id=id)})


def Search(request, query):
  job = Jobs.objects.filter(Client_Name__icontains=query).all()
  return render(request, "Jobs/jobSearch.html", {"jobs":job, "name":query})

# class SearchResultsView(ListView):
#     model = Jobs
#     template_name = "Jobs/jobSearch.html"

#     def get_queryset(self): # new
#         return Jobs.objects.filter(
#             Q(Client_Name__icontains="fe") | Q(state__icontains="NY")
#         )