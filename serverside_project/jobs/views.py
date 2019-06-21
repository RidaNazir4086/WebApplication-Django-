from django.shortcuts import render
from .models import Job , applicant
from  .forms import Job_form
from user_profile.models import UserSkill
from django.contrib.auth.models import User


# Create your views here.
def jobs(request):
    jobInstance = Job.objects.all()
    return render(request ,'jobs/jobs.html', {"jobInstance": jobInstance})

def applications(request):
    return render(request,'jobs/jobs.html')

def jobRequestForm_view(request): # for posting job
    form = Job_form(request.POST or None)
    if form.is_valid():
        form.save(user=request.user, commit=False)

    context = {
        'form': form
    }
    return render(request, 'jobs/postJob.html', context)


def jobApplicant_view(request):
    jobId= request.POST.get('jobId')
    user = User.objects.get(username=request.user)
    applicant.objects.create(job=Job(id=jobId), user=user)
    jobObj= Job.objects.get(id=jobId)
    jobObj.noOfApplicants += 1
    jobObj.save()
    return render(request, 'jobs/jobs.html')

def jobRelevancy_view(request):
    userSkills = UserSkill.objects.filter(user=request.user)

    for i in userSkills:
        jobs = Job.objects.filter(reqSkills = i.skill)

    context = {
        'relevantJobs' : jobs ,
    }
    return render(request, 'jobs/relevantJobs.html', context)


