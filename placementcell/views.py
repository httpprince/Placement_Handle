from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def pdashboard(request):
    return render(request,'Placementcell/index.html')


def addcompany(request):
    if request.method =='POST':
        uname=request.POST['username']
        cname=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=uname):
            messages.success(request, "Ueername Already Registered!!!")
            return render(request, 'Placementcell/addcompany.html')
            print('yyyyyyyy')
        if User.objects.filter(email=email):
            messages.success(request, "E-mail Already Registered!!!")
            return render(request, 'Placementcell/addcompany.html')
            print('yyyyyyyy')

        else:
            user=User.objects.create_user(username=uname,email=email,password=password)
            user.save()

            p=Company(
                user=user,
                is_company=True,
                name=cname,
                url=url,
            )
            p.save()
            return redirect('/placementcell/viewcompany/')

    return render(request ,'Placementcell/addcompany.html')



def viewcompany(request):
    c=Company.objects.all()
    return render(request,'Placementcell/viewcompany.html',{'c':c})



def addstudent(request):
    if request.method =='POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        eno=request.POST['e_no']
        gender=request.POST['gender']
        password=request.POST['password']
        if User.objects.filter(username=uname):
            messages.success(request, "Ueername Already Registered!!!")
            return render(request, 'Placementcell/addstudent.html')
            print('yyyyyyyy')
        if Student.objects.filter(e_no=eno):
            messages.success(request, "E-no is  Already Added!!!")
            return render(request, 'Placementcell/addstudent.html')
            print('yyyyyyyy')

        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,password=password)
            user.save()

            p=Student(
                user=user,
                e_no=eno,
                is_student=True,
                gender=gender,

            )
            p.save()
            return redirect('/placementcell/viewstudent/')

    return render(request ,'Placementcell/addstudent.html')


def viewstudent(request):
    s=Student.objects.all()

    return render(request,'Placementcell/viewstudent.html',{'s':s})
