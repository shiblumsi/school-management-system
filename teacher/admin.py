from django.contrib import admin
from .models import Teacher,Department
# Register your models here.


@admin.register(Department)
class TeachersDepartmentModeladmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Teacher)
class TeacherModeladmin(admin.ModelAdmin):
    list_display = ['id','user','name','department']