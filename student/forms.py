from django import forms
from .models import ClassRoom,Subject,RoutineTimeSlot

class GetStudentsForm(forms.Form):
    class_code = forms.CharField(max_length=255)


class GetSubjectsForm(forms.Form):
    student_id = forms.CharField(max_length=255)


class GetResultForm(forms.Form):
    student_id = forms.CharField(max_length=255)
    exam_type = forms.CharField(max_length=255)
    year = forms.IntegerField()


class WhichClassRoutineForm(forms.Form):
    which_class = forms.CharField(max_length=255)

class CreateRoutineForm(forms.Form):
    DAY = (
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
    )
    class_type = 1
    
    which_class = forms.ModelChoiceField(queryset=ClassRoom.objects.all())
    day = forms.ChoiceField(choices=DAY)
    first_class = forms.ModelChoiceField(queryset=Subject.objects.filter(which_class=class_type))
    second_class = forms.ModelChoiceField(queryset=Subject.objects.filter(which_class=class_type))
    third_class = forms.ModelChoiceField(queryset=Subject.objects.filter(which_class=class_type))
    fourth_class = forms.ModelChoiceField(required=False,queryset=Subject.objects.filter(which_class=class_type))
    fifth_class = forms.ModelChoiceField(required=False,queryset=Subject.objects.filter(which_class=class_type))
    sixth_class = forms.ModelChoiceField(required=False,queryset=Subject.objects.filter(which_class=class_type))
    
    

    
    
    
    
    
    