from django.contrib import admin
from .models import Class, ClassRoutineTimeSlot, Subject, ClassRoutine2

@admin.register(Class)
class ClassRoomModeladmin(admin.ModelAdmin):
    list_display = ['id','class_name','class_code']

@admin.register(Subject)
class SubjectModeladmin(admin.ModelAdmin):
    list_display = ['which_class','subject_name','subject_teacher']


@admin.register(ClassRoutineTimeSlot)
class RoutineTimeModeladmin(admin.ModelAdmin):
    list_display = ['id','routine_time_slot']

@admin.register(ClassRoutine2)
class RoutineTimeModeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','time_slot','subject','day','subject_teacher']
