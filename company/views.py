from django.shortcuts import render, redirect
from .models import *
from placementcell.models import Company



# Create your views here.
def cdashborad(request):
  return render(request, 'company/index.html')


def addjob(request):
  user = request.user.id
  company = Company.objects.get(user=user)
  print(company)

  if request.method == 'POST':
    title = request.POST['title']
    position = request.POST['position']
    category = request.POST['category']
    type = request.POST['type']
    description = request.POST['description']
    noofvacancy = request.POST['noofvacancy']
    exp = request.POST['exp']
    lastdateofapply = request.POST['lastdateofapply']
    salary = request.POST['salary']
    country = request.POST['country']
    state = request.POST['state']
    city = request.POST['city']
    tag = request.POST['tag']
    print(title, position, category, type, description, noofvacancy, exp,
          lastdateofapply, salary, country, state, country, state, city, tag)

    j = Job.objects.create(company_id=company.id, title=title, position=position, category=category, type=type,
                           description=description, noofvacancy=noofvacancy, exp=exp,
                           lastdateofapply=lastdateofapply, salary=salary, country=country,
                           state=state, city=city, tag=tag)
    return redirect('/company/addjob/')
  return render(request, 'company/addjob.html')


def joblist(request):
  j = Job.objects.all()
  return render(request, 'company/joblist.html', {'j': j})
