from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    from_Year = models.CharField(max_length=4)

    #end_Year = models.CharField(max_length=4)


class UserSkill(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    skill= models.CharField(max_length=50)

class UserExperience(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    Experience = models.CharField(max_length=50)

class UserInterest(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    Interest = models.CharField(max_length=50)

class UserProject(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    Title=  models.CharField(max_length=50)
    Course = models.CharField(max_length=50)
    Description=  models.CharField(max_length=200)



