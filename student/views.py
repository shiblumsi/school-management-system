from datetime import datetime
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse 
from .models import Mark, Student,Attendance,Class
from .forms import EditAttendanceForm, GetStudentsForm, GetSubjectsForm
from academic.models import ClassRoutine2


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


def students_attendance(request,class_id):
    class_obj = Class.objects.get(id=class_id)
    students = Student.objects.filter(which_class=class_obj)
    if request.method == "POST":
        for student in students:
            status = request.POST.get(f'student_{student.id}')
            date = request.POST.get('date')
            Attendance.objects.create(student=student,status=status,date=date)
    return render(request,'attendance.html',{'students':students,'class':class_obj})


def view_attendance(request, class_id):
    class_obj = Class.objects.get(id=class_id)
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        date = request.POST.get('date')
        date2 = request.POST.get('date2')
        if date:
            attendances = Attendance.objects.filter(date=date,student__id=student_id)
            return render(request, 'view_attendance.html', {'class': class_obj,'attendances': attendances})
        else:
            attendances = Attendance.objects.filter(student__which_class=class_obj,date=date2)
            return render(request, 'view_attendance.html', {'class': class_obj, 'attendances': attendances})
    return render(request, 'view_attendance.html')



def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == 'POST':
        form = EditAttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('teacher-deshboard')
    else:
        form = EditAttendanceForm(instance=attendance)
    return render(request, 'edit_attendance.html', {'form': form,'student_name':attendance.student.name})


def student_view_routine(request,class_id):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    routine = ClassRoutine2.objects.filter(which_class=class_id)
    context = {
        'routine':routine,
        'days':days,
        }
    return render(request,'student_view_routine.html',context)


def student_routine_today(request,class_id):
    today = datetime.now()
    day_of_week = today.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today_name = days[day_of_week]
    routine = ClassRoutine2.objects.filter(which_class=class_id).filter(day=today_name)   #authentication will apply
    context = {
        'routine':routine,
        'today':today_name,
        'days':days,
        }
    return render(request,'student_routine_today.html',context)


def view_result(request,student_id):
    student = Student.objects.get(id=student_id)
    results = Mark.objects.filter(student__id=student_id)
    context = {
        'results':results,
        'student':student
    }
    return render(request,'get_result.html',context)