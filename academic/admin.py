from django.contrib import admin
from .models import Class, ClassRoutine, ExamType, ClassRoutineTimeSlot, Subject, ClassRoutine2

@admin.register(Class)
class ClassRoomModeladmin(admin.ModelAdmin):
    list_display = ['id','class_name','class_code']

@admin.register(Subject)
class SubjectModeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','subject_name']

@admin.register(ExamType)
class ExamTypeModeladmin(admin.ModelAdmin):
    list_display = ['id','type','year']

# @admin.register(Result)
# class ResultModeladmin(admin.ModelAdmin):
#     list_display = ['id','exam_type','student','subject','mark','get_grade']

@admin.register(ClassRoutine)
class RoutineModeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','day','first_class']

@admin.register(ClassRoutineTimeSlot)
class RoutineTimeModeladmin(admin.ModelAdmin):
    list_display = ['id','routine_time_slot']

@admin.register(ClassRoutine2)
class RoutineTimeModeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','time_slot','subject','teacher','day']