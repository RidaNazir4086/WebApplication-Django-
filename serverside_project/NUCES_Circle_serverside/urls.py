"""NUCES_Circle_serverside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.conf.urls import url
#from user_profile.views import education_form_view
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login ,name='login'),
    path('home/', include('nuces_circle.urls')),
    path('jobs/', include('jobs.urls')),
    path('accounts/', include('accounts.urls')),
    path('networks/', include('networks.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('api/', include(router.urls)),
   # path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),

]
