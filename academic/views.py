from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ValidationError
from django.db.models import Q

from .forms import CreateClassRoutineForm, TutionFeeForm, WhichClassRoutineForm
from .models import ClassRoutine2,ExamRoutine, TutionFee


def create_class_routine(request):
    form = CreateClassRoutineForm()
    if request.method == "POST":
        form = CreateClassRoutineForm(request.POST)
        if form.is_valid():
            which_class=form.cleaned_data['for_class']
            time_slot=form.cleaned_data['time_slot']
            subject=form.cleaned_data['subject']
            day=form.cleaned_data['day']
            print(form.cleaned_data)
            teacher = subject.subject_teacher
            
            if ClassRoutine2.objects.filter(Q(time_slot=time_slot) & Q(subject__subject_teacher=teacher) & Q(day=day)).exists():
                raise ValidationError("Teacher was taken this day and time_slot ")
            else:
                ClassRoutine2.objects.create(
                    which_class=which_class,
                    time_slot=time_slot,
                    subject=subject,
                    day=day
                    )
                context = {
                    'form':form,
                }
            return render(request,'create_class_routine.html',context)
    return render(request,'create_class_routine.html',{'form':form})


def view_class_routine(request,class_id):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    routine = ClassRoutine2.objects.filter(which_class=class_id)
    context = {
        'routine':routine,
        'days':days,
        }
    return render(request,'student_view_routine.html',context)


 # have to modify
def view_exam_routine(request):
    routines = ExamRoutine.objects.all()        
    return render(request,'view_exam_routine.html',{'routines':routines})


def tution_fee(request,student_id):
    try:
        tf = get_object_or_404(TutionFee, student__id=student_id, month='MAY')
        if request.method == "POST":
            add_amount = request.POST.get('add_amount')
            tf.amount += int(add_amount)
            tf.save()
            if tf.amount >= 10000:
                tf.is_paid = True
                tf.save()
        context = {
            'tf':tf,
        }
        return render(request,'tution_fee_page.html',context)
    except:
        context = {
            'tf':None
        }
        return render(request,'tution_fee_page.html',context)
    

def view_tution_fee(request,student_id):
    tution_fees = TutionFee.objects.filter(student__id=student_id)
    context = {
        'tution_fees':tution_fees
    }
    return render(request,'view_tution_fee.html',context)