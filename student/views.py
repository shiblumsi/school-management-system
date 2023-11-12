import calendar
from datetime import datetime
from django.shortcuts import redirect, render,get_object_or_404,HttpResponse 
from .models import Mark, Student,Attendance,Class
from .forms import EditAttendanceForm, GetStudentsForm, GetSubjectsForm, StudentUpdateForm
from academic.models import ClassRoutine2
from django.contrib.auth import authenticate,login
from django.contrib import messages

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

def student_deshboard(request):
    user = request.user
    student = Student.objects.get(user__id=user.id)
    context = {
        'student':student,
    }
    return render(request,'student_deshboard.html',context)


def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login successful.')
            return redirect('student-deshboard')
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
    return render(request,'student_login.html')


def update_student_profile(request,student_id):
    student_obj = Student.objects.get(user__id=student_id)
    form = StudentUpdateForm(instance=student_obj)
    if request.method == "POST":
        form = StudentUpdateForm(request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect('student-deshboard')
    return render(request,'student_update_profile.html',{'form':form})
    

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


def student_view_attendance(request,student_id):
    month_nubmer = datetime.now().month
    month_name = calendar.month_name[month_nubmer]
    attendance = Attendance.objects.filter(date__month=month_nubmer,student__id=student_id)
    context = {
        'attendances':attendance,
        'month':month_name
        }
    return render(request,'student_view_attendance.html',context)


def student_view_all_attendance(request,student_id):
    months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
    ]
    attendance_list = []
    for i in range(1,13):
        attendance = Attendance.objects.filter(date__month=i,student__id=student_id)
        attendance_list.append(attendance)
    context = {
        'attendance_list':attendance_list,
        'months':months
        }
    return render(request,'student_view_all_attendance.html',context)


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
    routine = ClassRoutine2.objects.filter(which_class=class_id).filter(day=today_name)
    context = {
        'routine':routine,
        'today':today_name,
        'days':days,
        }
    return render(request,'student_routine_today.html',context)


def view_result(request,student_id):
    student = Student.objects.get(id=student_id)
    half_Yearly_exam_marks = Mark.objects.filter(student__id=student_id,term__id=1)
    final_exam_marks = Mark.objects.filter(student__id=student_id,term__id=2)
    half_Yearly_exam_marks=None
    context = {
        'half_Yearly_exam_marks':half_Yearly_exam_marks,
        'student':student,
        'final_exam_marks':final_exam_marks
    }
    return render(request,'get_result.html',context)