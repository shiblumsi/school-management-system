from django.contrib import admin
from .models import Student,Attendance,Mark
# Register your models here.

@admin.register(Student)
class StudentModeladmin(admin.ModelAdmin):
    list_display = ['id','user','name','which_class']


@admin.register(Attendance)
class AttendanceModeladmin(admin.ModelAdmin):
    list_display = ['id','student','status','date']


@admin.register(Mark)
class MarkModeladmin(admin.ModelAdmin):
    list_display = ['id','student','term','subject','mark']