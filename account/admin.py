from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CustomUser)
class CustomUserModeladmin(admin.ModelAdmin):
    list_display = ['id','username','is_superuser','is_staff','is_teacher','is_student']

