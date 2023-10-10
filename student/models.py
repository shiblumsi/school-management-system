from django.db import models
from account.models import CustomUser
from teacher.models import Teacher


class ClassRoom(models.Model):
    class_name = models.CharField(max_length=255)
    class_code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.class_name}'


class RoutineTimeSlot(models.Model):
    class_time = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.class_time

class Subject(models.Model):
    which_class = models.ForeignKey(ClassRoom,on_delete=models.CASCADE,related_name='which_class')
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    subject_teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    time_slot = models.ForeignKey(RoutineTimeSlot,on_delete=models.SET_NULL,null=True,blank=True,related_name='time_slot')

    def __str__(self) -> str:
        return f'{self.subject_name},{self.subject_code}'


class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    which_class = models.ForeignKey(ClassRoom,on_delete=models.CASCADE,blank=True)
    #status = models.CharField(max_length=255,choices='STATUS')

    def __str__(self) -> str:
        return self.name


class ExamType(models.Model):
    type = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self) -> str:
        return self.type


class Result(models.Model):
    exam_type = models.ForeignKey(ExamType,on_delete=models.CASCADE,related_name='results')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='results')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='results')
    mark = models.DecimalField(max_digits=3,decimal_places=1)

    def get_grade(self):
        if self.mark >= 80:
            return 'A+'
        if self.mark >= 70:
            return 'A'
        if self.mark >= 60:
            return 'B'
        if self.mark >= 50:
            return 'C'
        if self.mark >= 40:
            return 'D'
        if self.mark < 40:
            return 'F'
        

#Class Routine

    
class ClassRoutine(models.Model):
    DAY = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
    )
    which_class = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    day = models.CharField(max_length=255,choices=DAY)
    first_class = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True,related_name='first_class')
    second_class = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True,related_name='second_class')
    third_class = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True,related_name='third_class')
    fourth_class = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True,related_name='fourth_class')
    fifth_class = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True,related_name='fifth_class')
    sixth_class = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True,related_name='sixth_class')
    
    class Meta:
        unique_together = ('which_class','day')
