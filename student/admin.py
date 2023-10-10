from django.contrib import admin
from .models import Student, ClassRoom, Subject, ExamType, Result, ClassRoutine, RoutineTimeSlot
# Register your models here.

@admin.register(Student)
class StudentModeladmin(admin.ModelAdmin):
    list_display = ['id','user','name','which_class']

@admin.register(ClassRoom)
class ClassRoomModeladmin(admin.ModelAdmin):
    list_display = ['id','class_name','class_code']

@admin.register(Subject)
class SubjectModeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','subject_name','subject_code','subject_teacher']

@admin.register(ExamType)
class ExamTypeModeladmin(admin.ModelAdmin):
    list_display = ['id','type','year']

@admin.register(Result)
class ResultModeladmin(admin.ModelAdmin):
    list_display = ['id','exam_type','student','subject','mark','get_grade']

@admin.register(ClassRoutine)
class RoutineModeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','day','first_class']

@admin.register(RoutineTimeSlot)
class RoutineTimeModeladmin(admin.ModelAdmin):
    list_display = ['id','class_time']