from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    jobType = models.CharField(max_length=20)
    noOfApplicants= models.IntegerField(default=0)
    company = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    reqSkills = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

