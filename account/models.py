from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from .managers import SmsUserManager


# User = get_user_model()
# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique=True, null=False,blank=False)
    email = models.EmailField(max_length=255,unique=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = SmsUserManager()


