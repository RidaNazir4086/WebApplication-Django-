from django.urls import path, include
from . import views

urlpatterns = [
    path('networks', views.networks, name='networks'),
    path('requesting', views.sendingRequest, name='requesting'),
    path('accepting' , views.acceptingRequest, name='accepting'),
    path('logout', views.logout, name='logout')

]
