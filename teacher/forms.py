from django import forms

from student.models import Mark
from teacher.models import Teacher


class DepartmentCreateForm(forms.Form):
    name = forms.CharField(max_length=222)

class EditMarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('mark',)

class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name',)
     