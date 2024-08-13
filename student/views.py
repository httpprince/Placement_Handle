from django.shortcuts import render
from company.models import Job
# Create your views here.
def sdashboard(request):
    return render(request,'student/index.html')

def joblist(request):
    j=Job.objects.all()
    return render(request,'student/joblist.html',{'j':j})
