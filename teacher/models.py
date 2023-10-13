from django.db import models
from account.models import CustomUser
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



class Teacher(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.name