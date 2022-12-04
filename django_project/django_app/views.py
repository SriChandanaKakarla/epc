

from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from .models import Employees
import math,random
# Create your views here.


def home(request):
    return render(request, "home.html")



# Create your views here.

def seeall(request):
    return render(request,'courses.html')
def login(request):
    if request.method=="POST":
        us=request.POST.get("u")
        passw=request.POST.get("p")
        user = authenticate(request ,  username=us, password=passw)

        if user is not None:

            return redirect("dashboard")

        else:
            return HttpResponse("errorr")
    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        EmpId = request.POST['mobileno']
        EmpName = request.POST['name']
        EmpGender = request.POST['username']
        EmpEmail = request.POST['email']
        EmpDesignation = request.POST['password']
        data = Employees(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail,
                        EmpDesignation=EmpDesignation)
        data.save()

        us = request.POST.get("username")
        passw = request.POST.get("password")
        e = request.POST.get("email")

        new_user = User.objects.create_user(us,e,passw)
        new_user.first_name=EmpName
        new_user.save()

        return redirect('pro')
    else:
        return render(request, 'register.html')

def show(request):
    employees = Employees.objects.all()
    return render(request,'show.html',{'employees':employees} )
def dashboard(request):
    return render(request,'dashboard.html')
def pro(request):
    return render(request,'pro.html')


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(request):
    email = request.GET.get("email")
    print(email)
    o = generateOTP()
    htmlgen = '<p>Your OTP is <strong>o</strong></p>'
    send_mail('OTP request', o, '<your gmail id>', [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)
def otp(request):
    return render(request,"otp.html")


# def login(request):
#     return render(request,'login.html')
#
# def register(request):
#     return render(request,'register.html')