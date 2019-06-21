from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class MyConnections(models.Model):
 #   person1 =


class requesting(models.Model):
     sendBy = models.ForeignKey(User, on_delete=models.CASCADE, default=1 , related_name='sendBy')
     sendTo = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='sendTo')
     accepted = models.BooleanField(default=False)
     requestSent = models.BooleanField(default=False)