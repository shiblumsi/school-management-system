from django.urls import path
from .views import get_students_by_class, get_subjects_by_student, get_result, class_routine, create_class_routine, students_attendance, view_attendance
urlpatterns = [
    path('sc',get_students_by_class),
    path('ss',get_subjects_by_student),
    path('sr',get_result),
    path('scr',class_routine),
    path('scrr',create_class_routine),
    path('sa/<int:id>',students_attendance),
    path('va/<int:class_id>',view_attendance),
]
