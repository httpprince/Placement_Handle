from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def adashboard(request):
    return render(request ,'adminapp/index.html')
def addplacementcell(request):
    if request.method =='POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=uname):
            messages.success(request, "Ueername Already Registered!!!")
            return render(request, 'adminapp/addplacementcells.html')
            print('yyyyyyyy')
        if User.objects.filter(email=email):
            messages.success(request, "E-mail Already Registered!!!")
            return render(request, 'adminapp/addplacementcells.html')
            print('yyyyyyyy')
        if len(fname) > 10 and len(lname) > 10:
            messages.success(request, "First or Last Name too long!!!")
            return render(request,'adminapp/addplacementcells.html' )
        if not fname.isalpha() or not lname.isalpha():
            messages.warning(request, "Name must contain only letters.")
            return render(request, 'adminapp/addplacementcells.html')
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
            user.save()

            p=Placement(
                user=user,
                is_Placement=True,
            )
            p.save()
            return redirect('/adminapp/viewplacementcells/')

    return render(request ,'adminapp/addplacementcells.html')


def viewplacementcells(request):
    p=Placement.objects.all()
    return render(request ,'adminapp/viewplacementcells.html',{'p':p})