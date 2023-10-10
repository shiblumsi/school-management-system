from django.shortcuts import render,HttpResponse

from django.contrib.auth import get_user_model
from .forms import TeacherCreationForm, StudentCreationForm

from teacher.models import Teacher,TeachersDepartment
from student.models import Student,ClassRoom
User = get_user_model()
# Create your views here.

def teacher_create(request):
    form = TeacherCreationForm()
    if request.method == "POST":
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            department_id = form.cleaned_data['department']
            user = User.objects.create_teacher(username=username,password=password,email=email)
            department = TeachersDepartment.objects.get(pk=department_id)
            Teacher.objects.create(user=user,name=name,department=department)
    return render(request,'teacher_create.html',{'form':form})


def student_create(request):
    form = StudentCreationForm()
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            class_code = form.cleaned_data['class_code']
            which_class = ClassRoom.objects.get(class_code=class_code)
            user = User.objects.create_student(username=username,password=password,email=email)
            Student.objects.create(user=user,name=name,which_class=which_class)
            
    return render(request,'student_create.html',{'form':form})


def superuser_create(request):
    user = User.objects.create_superuser(username='admin',email='admin@gmail.com',password='1')
    print(user)
    return HttpResponse('hi')