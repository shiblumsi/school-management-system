from django.contrib import admin
from .models import Class, ClassRoutineTimeSlot, Subject, ClassRoutine2,ExamTimeSlot,ExamType,ExamRoutine,Result,TutionFeeByClass,TutionFee

@admin.register(Class)
class ClassModeladmin(admin.ModelAdmin):
    list_display = ['id','class_name','class_code']

@admin.register(Subject)
class SubjectModeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','subject_name','subject_teacher']


@admin.register(ClassRoutineTimeSlot)
class ClassRoutineTimeSlotModeladmin(admin.ModelAdmin):
    list_display = ['id','routine_time_slot']

@admin.register(ClassRoutine2)
class ClassRoutine2Modeladmin(admin.ModelAdmin):
    list_display = ['id','which_class','time_slot','subject','day','subject_teacher']

@admin.register(ExamTimeSlot)
class ExamTimeSlotModeladmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(ExamType)
class ExamTypeModeladmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(ExamRoutine)
class ExamRoutineModeladmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Result)
class ResultModeladmin(admin.ModelAdmin):
    list_display = ['student','subject','mark']



@admin.register(TutionFeeByClass)
class TutionFeeByClassModeladmin(admin.ModelAdmin):
    list_display = ['which_class','tution_fee']



@admin.register(TutionFee)
class TutionFeeModeladmin(admin.ModelAdmin):
    list_display = ['student','amount','month','payment_date','due_amount','is_paid']