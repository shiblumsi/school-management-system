from django.shortcuts import render,HttpResponse

from django.contrib.auth import get_user_model
from .forms import TeacherCreationForm, StudentCreationForm

from teacher.models import Teacher,Department
from student.models import Student,Class
User = get_user_model()
# Create your views here.

def index(request):
    return render(request,'index.html')

def teacher_create(request):
    form = TeacherCreationForm()
    if request.method == "POST":
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            department_name = form.cleaned_data['department']
            user = User.objects.create_teacher(username=name,password='1',email=email)
            department = Department.objects.get(name=department_name)
            Teacher.objects.create(user=user,name=name,department=department)
    return render(request,'teacher_create.html',{'form':form})


def student_create(request):
    form = StudentCreationForm()
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            class_code = form.cleaned_data['class_code']
            which_class = Class.objects.get(class_code=class_code)
            user = User.objects.create_student(username=name,password='1',email=email)
            Student.objects.create(user=user,name=name,which_class=which_class)
            
    return render(request,'student_create.html',{'form':form})


def superuser_create(request):
    user = User.objects.create_superuser(username='admin',email='admin@gmail.com',password='1')
    print(user)
    return HttpResponse('hi')