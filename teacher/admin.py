from django.contrib import admin
from .models import Teacher,TeachersDepartment
# Register your models here.

@admin.register(Teacher)
class TeacherModeladmin(admin.ModelAdmin):
    list_display = ['id','user','name','department']


@admin.register(TeachersDepartment)
class TeachersDepartmentModeladmin(admin.ModelAdmin):
    list_display = ['id','department_name']