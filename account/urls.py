from django.urls import path
from .views import teacher_create,student_create,superuser_create

urlpatterns = [
    path('t',teacher_create),
    path('s',student_create),
    path('su',superuser_create),
]
