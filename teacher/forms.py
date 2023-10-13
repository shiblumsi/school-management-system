from django import forms


class DepartmentCreateForm(forms.Form):
    name = forms.CharField(max_length=222)
