from django import forms
from .models import Attendance

class GetStudentsForm(forms.Form):
    class_code = forms.CharField(max_length=255)


class GetSubjectsForm(forms.Form):
    student_id = forms.CharField(max_length=255)


class EditAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'status']