from django import forms
from teacher.models import Department

class TeacherCreationForm(forms.Form):
    # username= forms.CharField(max_length=100)
    # password= forms.CharField(max_length=255)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    
class StudentCreationForm(forms.Form):
    username= forms.CharField(max_length=100)
    password= forms.CharField(max_length=255)
    email = forms.EmailField()
    name= forms.CharField(max_length=100)
    class_code = forms.CharField(max_length=100)
    