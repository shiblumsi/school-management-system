# def student_create(request):
#     form = StudentCreationForm()
#     if request.method == "POST":
#         form = StudentCreationForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             class_code = form.cleaned_data['class_code']
#             which_class = Class.objects.get(class_code=class_code)
#             user = User.objects.create_student(username=name,password='1',email=email)
#             Student.objects.create(user=user,name=name,which_class=which_class)
            
#     return render(request,'student_create.html',{'form':form})

from django.contrib.auth import get_user_model

from teacher.models import Department, Teacher
User = get_user_model()
from student.models import Student
from django.shortcuts import HttpResponse
from academic.models import Class

def fack_create(request):
    X = 'stu1'
    for i in range(1,11):
        user = User.objects.create_student(username=f'{X}{i}',password='1',email=f'{X}{i}@gmail.com')
        Student.objects.create(user=user,name=f'{X}{i}',which_class=Class.objects.get(class_code='01'))
    return HttpResponse('created')


# def fack_create(request):
#     name = 'sTeacher'
#     department = Department.objects.get(name="Science")
#     for i in range(1,5):
#         user = User.objects.create_teacher(username=f'{name}{i}',password='1',email=f'{name}{i}@gmail.com')
#         Teacher.objects.create(user=user,name=f'{name}{i}',department=department)
#     return HttpResponse('created')