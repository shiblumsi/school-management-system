from django import forms
from .models import Attendance, Student

class GetStudentsForm(forms.Form):
    class_code = forms.CharField(max_length=255)


class GetSubjectsForm(forms.Form):
    student_id = forms.CharField(max_length=255)


class EditAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'status']


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name',)