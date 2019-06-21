from django.shortcuts import render
from django.contrib.auth.models import User
from .models import requesting
from django.contrib import auth


# Create your views here.
def networks(request):
    people = User.objects.all()
    sendToUsers = requesting.objects.filter(sendBy=request.user)
    sendByUsers = requesting.objects.filter(sendTo=request.user)

    id = [s.sendTo.id for s in sendToUsers ]
    idBy = [s.sendTo.id for s in sendByUsers]

    for i in idBy:
        print(i)
    context = {
        'people': people ,
        'sendToUsers' : sendToUsers,
        'id': id ,
         'idBy': idBy,
    }
    return render(request,'networks/my_networks.html', context)

def sendingRequest(request):
    sendTo = request.POST.get('sendTo')
    sendToUser = User.objects.get(username=sendTo)
    user=User.objects.get(username=request.user)
    requesting.objects.create(sendBy=user, sendTo=sendToUser, requestSent= True)
    return render(request, 'networks/my_networks.html')

def acceptingRequest(request):
    sendToUsers = requesting.objects.filter(sendBy=request.user)
    context = {
        'sendToUsers': sendToUsers ,
    }
    print( sendToUsers )
    return render(request, 'networks/my_networks.html', context)


def logout(request):
    if request.method == 'POST':
       auth.logout(request)
       return render(request, 'accounts/login.html')