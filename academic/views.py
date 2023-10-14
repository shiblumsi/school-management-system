from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db.models import Q

from .forms import CreateClassRoutineForm, WhichClassRoutineForm
from .models import ClassRoutine2


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
    routine = ClassRoutine2.objects.filter(which_class__id=class_id)
    return render(request,'class_routine.html',{'routine':routine})