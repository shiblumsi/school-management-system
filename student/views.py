from django.shortcuts import render,get_object_or_404,HttpResponse 
from .models import Student, ClassRoom, Subject , Result, ClassRoutine, RoutineTimeSlot
from .forms import GetStudentsForm, GetSubjectsForm, GetResultForm, CreateRoutineForm, WhichClassRoutineForm
# Create your views here.
def student_detail(request):
    pass

def get_students_by_class(request):
    form = GetStudentsForm()
    if request.method == "POST":
        form = GetStudentsForm(request.POST)
        if form.is_valid():
            class_code = form.cleaned_data['class_code']
        students = Student.objects.filter(which_class=class_code)

        context = {
            'students': students,
            'form':form
        }
        return render(request,'get_students_by_class.html',context)
    return render(request,'get_students_by_class.html',{'form':form})

def get_subjects_by_student(request):
    form = GetSubjectsForm()
    if request.method == "POST":
        form = GetSubjectsForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
        stu = Student.objects.get(pk=student_id)
        subjects = stu.which_class.which_class.all()
        context = {
            'student':stu,
            'subjects':subjects,
            'form':form
        }
        return render(request,'get_subjects_by_student.html',context)
    return render(request,'get_subjects_by_student.html',{'form':form})


def get_result(request):
    form = GetResultForm()
    if request.method == "POST":
        form = GetResultForm(request.POST)
        if form.is_valid():
            stu_id = form.cleaned_data['student_id']
            year = form.cleaned_data['year']
            exam_type = form.cleaned_data['exam_type']
            result = Result.objects.filter(student__id=stu_id,exam_type__type=exam_type)
            student = Student.objects.get(pk=stu_id)
            context = {
                'result':result,
                'student':student,
                'year':year,
                'exam_type':exam_type,
                'form':form
            }
        return render(request,'get_result.html',context)
    return render(request,'get_result.html',{'form':form})


def create_class_routine(request):
    form = CreateRoutineForm()
    if request.method == "POST":
        form = CreateRoutineForm(request.POST)
        if form.is_valid():
            which_class = form.cleaned_data['which_class']
            day = form.cleaned_data['day']
            first_class = form.cleaned_data['first_class']
            second_class = form.cleaned_data['second_class']
            third_class = form.cleaned_data['third_class']
            fourth_class = form.cleaned_data['fourth_class']
            fifth_class = form.cleaned_data['fifth_class']
            sixth_class = form.cleaned_data['sixth_class']
            if ClassRoutine.objects.filter(day=day).exists():
                raise ValueError("error")
            ClassRoutine.objects.create(which_class=which_class,day=day,first_class=first_class,second_class=second_class,third_class=third_class,fourth_class=fourth_class,fifth_class=fifth_class,sixth_class=sixth_class)
        context = {
            'form':form
        }
        return render(request,'create_routine.html',context)
    return render(request,'create_routine.html',{'form':form})


def class_routine(request):
    form = WhichClassRoutineForm()
    if request.method == "POST":
        form = WhichClassRoutineForm(request.POST)
        if form.is_valid():
            which_class = form.cleaned_data['which_class']
        routine = ClassRoutine.objects.filter(which_class=which_class)
        print (routine[0].first_class.time_slot)
        
        context = {
            'routine':routine,
            'form':form,
           
        }
        return render(request,'class_routine.html',context)
    return render(request,'class_routine.html',{'form':form})
        
