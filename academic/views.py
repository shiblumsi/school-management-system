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
            teacher=form.cleaned_data['teacher']
            day=form.cleaned_data['day']
            print(form.cleaned_data)
            
            if ClassRoutine2.objects.filter(Q(time_slot=time_slot) & Q(teacher=teacher) & Q(day=day)).exists():
                raise ValidationError("Teacher was taken this day and time_slot ")
            else:
                ClassRoutine2.objects.create(
                    which_class=which_class,
                    time_slot=time_slot,
                    subject=subject,
                    teacher=teacher,
                    day=day
                    )
                context = {
                    'form':form,
                }
            return render(request,'create_class_routine.html',context)
    return render(request,'create_class_routine.html',{'form':form})