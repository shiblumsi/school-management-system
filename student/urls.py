from django.urls import path
from .views import get_students_by_class, get_subjects_by_student, students_attendance, view_attendance
urlpatterns = [
    path('sc',get_students_by_class),
    path('ss',get_subjects_by_student),
    path('sa/<int:id>',students_attendance),
    path('va/<int:class_id>',view_attendance),
]
