from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from academic.models import ExamType, Subject
from student.models import Mark, Student
from .forms import DepartmentCreateForm, EditMarkForm
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


def teacher_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login successful.')
            return redirect('teacher-deshboard')
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
    return render(request,'teacher_login.html')


def teacher_deshboard(request):
    user = request.user
    teacher = Teacher.objects.get(user=user)
    subject = Subject.objects.filter(subject_teacher=teacher)
    context = {
        'user':user,
        'subject':subject
    }
    return render(request,'teacher_deshboard.html',context)


def teacher_gives_mark(request):
    subjects = Subject.objects.filter(subject_teacher__id=4)
    print(subjects)
    context = {
        'subjects':subjects,
    }
    return render(request,'teacher_gives_mark.html',context)


def give_mark(request,subject_id):
    subject = Subject.objects.get(id=subject_id)
    students = Student.objects.filter(which_class=subject.which_class)
    if request.method == "POST":
        type = request.POST.get('exam_type')
        exam_type = ExamType.objects.get(exam_type=type)
        for student in students:
            mark = request.POST.get(f'student_{student.id}')
            Mark.objects.create(term=exam_type,subject=subject,mark=mark,student=student)
    return render(request,'give_mark.html',{'students':students,'subject':subject})

def view_mark(request,subject_id):
    subject = Subject.objects.get(id=subject_id)
    marks = Mark.objects.filter(subject=subject, student__which_class=subject.which_class)
    return render(request,'view_mark.html',{'marks':marks})


def edit_mark(request,mark_id):
    mark_obj = get_object_or_404(Mark,id=mark_id)
    if request.method == "POST":
        form = EditMarkForm(request.POST, instance=mark_obj)
        if form.is_valid():
            form.save()
            return redirect('teacher-deshboard')
    else:
        form = EditMarkForm(instance=mark_obj)
    return render(request,'edit_mark.html',{'form':form})


def get_highest_mark(request,subject_id):
    subject_obj = Subject.objects.get(id=subject_id)
    term = ExamType.objects.get(id=1)
    highest_mark = None
    how_many = None
    if request.method == "POST":
        how_many = request.POST.get('how_many')
        highest_mark = Mark.objects.filter(subject=subject_obj,term=term).order_by('-mark')[:int(how_many)]
    return render(request,'get_highest_mark.html',{'highest_marks':highest_mark,'how_many':how_many})