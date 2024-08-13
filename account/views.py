from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from adminapp.models import Placement

from placementcell.models import Company,Student


# Create your views here.
def signin(request):
    current_user = request.user
    if current_user.id:
        if User.objects.filter(username=current_user,is_superuser=True):
            messages.success(request, 'Already logged in!!!')
            return redirect('/adminapp/')

        if Placement.objects.filter(user=current_user, is_Placement=True):
            print('pllllllllllllaaaaaaaaaaaaaaaaa')

            messages.success(request, 'Already logged in!!!')
            return redirect('/placementcell/')
        if Company.objects.filter(user=current_user, is_company=True):


            messages.success(request, 'Already logged in!!!')
            return redirect('/company/')
        if Student.objects.filter(user=current_user,is_student=True):
            print('student')

            messages.success(request, 'Already logged in!!!')
            return redirect('/student/')





    if request.method =='POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None:

            if authenticate(request, username=uname, password=password).is_superuser:
                print('admin here')
                user = authenticate(request, username=uname, password=password,is_superuser=True)
                if user is not None:
                    login(request, user)
                    return redirect('/adminapp/')
            elif Placement.objects.filter(user=user,is_Placement=True):
                 login(request, user)
                 return redirect('/placementcell/')
                 print('placement')
            elif Company.objects.filter(user=user,is_company=True):
                 login(request, user)
                 return redirect('/company/')
                 print('company')
            elif Student.objects.filter(user=user,is_student=True):
                 login(request, user)
                 return redirect('/student/')
                 print('student')

        else:
            messages.warning(request, "username or Password Incorrect!!!")
            return render(request, 'account/signin.html', )
    return render(request,'account/signin.html')


def signout(request):
    logout(request)
    return redirect('/')