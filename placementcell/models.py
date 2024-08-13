from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    logo=models.ImageField(upload_to='companylogo',default='clogo.png')
    is_company=models.BooleanField(default=False)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.url.startswith('https://'):
            raise ValidationError("URL must start with 'https://'")


class Student(models.Model):
    g=(('m','male'),
       ('f','female'))
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    e_no=models.CharField(max_length=50,unique=True)
    gender=models.CharField(choices=g,max_length=50)
    is_student=models.BooleanField(default=False)

    def __str__(self):
        return self.e_no





