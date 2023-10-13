from django.shortcuts import render
from .forms import DepartmentCreateForm
from .models import Teacher, Department

# Create your views here.

def create_department(request):
    form = DepartmentCreateForm()
    if request.method == "POST":
        form = DepartmentCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Department.objects.create(name=name)
            
    return render(request,'department.html',{'form':form})
