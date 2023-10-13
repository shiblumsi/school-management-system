from django import forms

class GetStudentsForm(forms.Form):
    class_code = forms.CharField(max_length=255)


class GetSubjectsForm(forms.Form):
    student_id = forms.CharField(max_length=255)
