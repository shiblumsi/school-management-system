from django.urls import path
from .views import get_students_by_class, get_subjects_by_student, students_attendance, view_attendance,student_view_routine,student_routine_today
urlpatterns = [
    path('sc',get_students_by_class),
    path('ss',get_subjects_by_student),
    path('sa/<int:id>',students_attendance),
    path('va/<int:class_id>',view_attendance),
    path('va/<int:class_id>',view_attendance),
    path('studentviewroutine/<int:class_id>',student_view_routine,name='student-view-routine'),
    path('studentroutinetoday/<int:class_id>',student_routine_today,name='student-today-routine'),
]
