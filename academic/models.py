from django.db import models
from sms_backend.utils import PreModel
from teacher.models import Teacher

# Create your models here.
class Class(PreModel):
    class_name = models.CharField(max_length=255)
    class_code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.class_name


class Subject(PreModel):
    which_class = models.ForeignKey(Class,on_delete=models.CASCADE,related_name='which_class')
    subject_name = models.CharField(max_length=255)
    subject_teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.subject_name}'



class ClassRoutineTimeSlot(PreModel):
    routine_time_slot = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.routine_time_slot


class ClassRoutine2(PreModel):
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


class TutionFeeByClass(PreModel):
    which_class = models.OneToOneField(Class,on_delete=models.CASCADE)
    tution_fee = models.PositiveIntegerField()


class TutionFee(PreModel):
    MONTH_CHOICES = [
        ('JANUARY', 'January'),
        ('FEBRUARY', 'February'),
        ('MARCH', 'March'),
        ('APRIL', 'April'),
        ('MAY', 'May'),
        ('JUNE', 'June'),
        ('JULY', 'July'),
        ('AUGUST', 'August'),
        ('SEPTEMBER', 'September'),
        ('OCTOBER', 'October'),
        ('NOVEMBER', 'November'),
        ('DECEMBER', 'December'),
    ]
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=255, choices=MONTH_CHOICES)
    payment_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    @property
    def due_amount(self):
        return self.amount - 10000





class ExamType(PreModel):
    exam_type = models.CharField(max_length=255)

    def __str__(self):
        return self.exam_type


class ExamTimeSlot(PreModel):
    time_slot = models.CharField(max_length=255)


class ExamRoutine(PreModel):
    date = models.DateField()
    #time_slot = models.ForeignKey(ExamTimeSlot,on_delete=models.CASCADE)
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
    
    

class Result(PreModel):
    student = models.ForeignKey('student.Student',on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    year = models.CharField(max_length=255)
    term = models.ForeignKey(ExamType,on_delete=models.CASCADE)
    mark = models.PositiveIntegerField()


