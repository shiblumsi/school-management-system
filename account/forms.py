from django import forms

class TeacherCreationForm(forms.Form):
    username= forms.CharField(max_length=100)
    password= forms.CharField(max_length=255)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)
    
class StudentCreationForm(forms.Form):
    username= forms.CharField(max_length=100)
    password= forms.CharField(max_length=255)
    email = forms.EmailField()
    name= forms.CharField(max_length=100)
    class_code = forms.CharField(max_length=100)
    