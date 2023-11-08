from django.urls import path
from .views import teacher_create,student_create,superuser_create, index
from .facker import fack_create

urlpatterns = [
    path('createteacher',teacher_create,name='create-teacher'),
    path('createstudent',student_create,name='create-student'),
    path('superuser',superuser_create,name='create-superuser'),
    path('',index,name='index'),
    path('fack_create',fack_create,name='fack_create')
]
