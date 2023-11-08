from django.db import models
from account.models import CustomUser
from academic.models import Class, ExamType, Subject



class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    which_class = models.ForeignKey(Class,on_delete=models.CASCADE,blank=True)
    #status = models.CharField(max_length=255,choices='STATUS')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    ATTENDANCE_STATUS = (
        ('Present','Present'),
        ('Absent','Absent'),
        ('Leave','Leave'),
    )
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=255,choices=ATTENDANCE_STATUS)

    def __str__(self) -> str:
        return f'{self.student.name}'


class Mark(models.Model):
    term = models.ForeignKey(ExamType,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject =models.ForeignKey(Subject,on_delete=models.CASCADE)
    mark = models.PositiveSmallIntegerField()
