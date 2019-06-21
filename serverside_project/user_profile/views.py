from django.shortcuts import render, get_object_or_404
from .forms import EducationForm, SkillForm ,UserProjectForm, UserInterestForm, UserExperienceForm
from .models import education, UserSkill , UserInterest , UserProject, UserExperience
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def user_profile(request):
    userEducation= education.objects.filter(user=request.user)
    puser=request.user
    userSkill= UserSkill.objects.filter(user=request.user)
    userInterest=UserInterest.objects.filter(user=request.user)
    userExperience= UserExperience.objects.filter(user=request.user)
    userProjects= UserProject.objects.filter(user= request.user)
    return render(request,'user_profile/profile.html',
                  {"user": puser , "userEducation": userEducation,"UserSkill": userSkill, "UserInterest":userInterest, "UserExperience":userExperience, "UserProject" : userProjects})



def education_form_view(request):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        form.save(user=request.user, commit=False)

    context = {
       'form': form
     }
    return render(request, 'user_profile/user_education.html', context)


def UserSkill_form_view(request):
    form = SkillForm(request.POST or None)
    if form.is_valid():
        form.save(user=request.user, commit=False)

    context = {
       'form': form
     }
    return render(request, 'user_profile/user_skills.html', context)

def UserInterest_form_view(request):
    form = UserInterestForm(request.POST or None)
    if form.is_valid():
        form.save(user=request.user, commit=False)

    context = {
       'form': form
     }
    return render(request, 'user_profile/user_interests.html', context)

def UserExperience_form_view(request):
    form = UserExperienceForm(request.POST or None)
    if form.is_valid():
        form.save(user=request.user, commit=False)

    context = {
       'form': form
     }
    return render(request, 'user_profile/user_experience.html', context)

def UserProjects_form_view(request):
    form = UserProjectForm(request.POST or None)
    if form.is_valid():
        form.save(user=request.user, commit=False)

    context = {
       'form': form
     }
    return render(request, 'user_profile/user_projects.html', context)
