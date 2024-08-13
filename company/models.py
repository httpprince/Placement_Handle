from django.db import models
from django.utils import timezone

from placementcell.models import Company


# Create your models here.
class Job(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    description=models.CharField(max_length=2000)
    noofvacancy=models.CharField(max_length=10)
    exp=models.CharField(max_length=50)
    lastdateofapply=models.DateTimeField()
    salary=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    tag=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now)
    is_published=models.BooleanField(default=False)
    is_closed=models.BooleanField(default=False)




