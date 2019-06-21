from django.urls import path, include
import jobs.views
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('posts', views.postForm_view, name='postForm'),
   # path('jobRequest', jobs.views.jobRequestForm_view, name="PostJob"),

]