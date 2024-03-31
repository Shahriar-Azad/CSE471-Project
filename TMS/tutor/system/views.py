from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    error = ""
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        try:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=email,password=password)
            TutorDetail.objects.create(user=user, gender = gender)
            error="no"
        except:
            error="yes"

    return render(request, 'register.html',locals())



def t_login(request):
    error = ""
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            error="no"
        else:
            error="yes"
    return render(request, 't_login.html',locals())


def t_home(request):
    return render(request, 't_home.html')



def visa(request):
    return render(request, 'visa.html')


def bkash(request):
    return render(request, "bkash.html")

def nagad(request):
    return render(request, "nagad.html")


def contact(request):
    return render(request, "contact.html")


# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'shahriar.azad123@gmail.com',
#     ['tasnimneha42@gmail.com'],
#     fail_silently=False,
# )

def video(request):
    obj = Item.objects.all()
    return render(request,'video.html',{'obj':obj})


def available(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Data.objects.filter(location__icontains=q)
    else:

        data = Data.objects.all()
    context = {
        'data':data

    }
    return render(request, "available.html",context)