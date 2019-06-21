from django.urls import path, include
from . import views


urlpatterns = [
    path('user_profile', views.user_profile, name='user_profile'),
    path('education', views.education_form_view, name="education_form"),
    path('UserSkill', views.UserSkill_form_view, name="skill_form"),
    path('UserInterests', views.UserInterest_form_view, name="interest_form"),
    path('UserExperience', views.UserExperience_form_view, name="experience_form"),
    path('UserProject', views.UserSkill_form_view, name="projects_form"),

]
