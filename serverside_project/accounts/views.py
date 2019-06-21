from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def signup(request):
    if request.method=='POST':
        if len(request.POST['password'])>= 8:
            try:
                # checking if user already exist or not
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'Error':'User Name Is Already In USE!!!'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],password=request.POST['password'], email=request.POST['email'])

                subject= 'Welcome to NUCES Circle'
                message= 'Thank you for joining NUCES Circle'
                from_email= settings.EMAIL_HOST_USER
                to_list= [request.POST['email'], settings.EMAIL_HOST_USER ]

                send_mail(subject, message, from_email, to_list, fail_silently=True )

                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'Error':'Password is too Short!!!'})

    else:
         return render(request,'accounts/signup.html')


def login(request):
    if request.method=='POST':
       user = authenticate(username=request.POST['username'], password= request.POST['password'])
       if user is not None:
       # A backend authenticated the credentials
          auth.login(request,user)
          return redirect('home')
       else:
       # No backend authenticated the credentials
          return render(request,'accounts/login.html',{'Error':'Password or User name is not Correct !!!'})

    else:
      return render(request,'accounts/login.html')

