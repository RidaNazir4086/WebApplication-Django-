from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('jobs', views.jobs ,name='jobs'),
    path('jobRequest', views.jobRequestForm_view, name="PostJob"),
    path('jobapplication', views.jobApplicant_view, name="jobapplication"),
    path('jobRelevancy', views.jobRelevancy_view, name= 'jobRelevancy'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
