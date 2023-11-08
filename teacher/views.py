from django.shortcuts import render

from academic.models import ExamType, Subject
from student.models import Mark, Student
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


def teacher_gives_mark(request):
    subjects = Subject.objects.filter(subject_teacher__id=5)
    print(subjects)
    context = {
        'subjects':subjects,
    }
    return render(request,'teacher_gives_mark.html',context)


def give_mark(request,subject_id):
    subject = Subject.objects.get(id=subject_id)
    students = Student.objects.filter(which_class=subject.which_class)
    if request.method == "POST":
        for student in students:
            mark = request.POST.get(f'student_{student.id}')
            Mark.objects.create(term=ExamType.objects.get(exam_type='Half_Yearly'),subject=subject,mark=mark,student=student)
    return render(request,'give_mark.html',{'students':students})

