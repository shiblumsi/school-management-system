from django import forms

from teacher.models import Teacher
from .models import  Class, ClassRoutineTimeSlot, Subject



class GetResultForm(forms.Form):
    student_id = forms.CharField(max_length=255)
    exam_type = forms.CharField(max_length=255)
    year = forms.IntegerField()


class WhichClassRoutineForm(forms.Form):
    which_class = forms.CharField(max_length=255)

class CreateClassRoutineForm(forms.Form):
    DAY = (
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
    )
    for_class = forms.ModelChoiceField(queryset=Class.objects.all())
    time_slot = forms.ModelChoiceField(queryset=ClassRoutineTimeSlot.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    day = forms.ChoiceField(choices=DAY)
  