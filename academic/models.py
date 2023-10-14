from django.db import models
from teacher.models import Teacher

# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=255)
    class_code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.class_name


class Subject(models.Model):
    which_class = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='which_class')
    subject_name = models.CharField(max_length=255)
    # subject_code = models.CharField(max_length=255)
    subject_teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    # time_slot = models.ForeignKey(RoutineTimeSlot,on_delete=models.SET_NULL,null=True,blank=True,related_name='time_slot')

    def __str__(self) -> str:
        return f'{self.subject_name}'



class ClassRoutineTimeSlot(models.Model):
    routine_time_slot = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.routine_time_slot


class ClassRoutine2(models.Model):
    DAY = (
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
    )

    which_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    time_slot = models.ForeignKey(ClassRoutineTimeSlot,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    day = models.CharField(max_length=255,choices=DAY)

    def subject_teacher(self):
        return self.subject.subject_teacher
    
    def __str__(self) -> str:
        return self.subject.subject_name


class ExamType(models.Model):
    exam_type = models.CharField(max_length=255)


class ExamTimeSlot(models.Model):
    time_slot = models.CharField(max_length=255)


class ExamRoutine(models.Model):
    date = models.DateField()
    time_slot = models.ForeignKey(ExamTimeSlot,on_delete=models.CASCADE)
    exam_type = models.ForeignKey(ExamType,on_delete=models.CASCADE)
    exam1 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam1')
    exam2 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam2')
    exam3 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam3')
    exam4 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam4')
    exam5 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam5')
    exam6 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam6')
    exam7 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam7')
    exam8 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam8')
    exam9 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam9')
    exam10 = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='exam10')