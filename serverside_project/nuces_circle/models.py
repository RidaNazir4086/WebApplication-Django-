from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True)

