from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Placement(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_Placement=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


