from django.urls import path
from .views import edit_attendance, get_students_by_class, get_subjects_by_student, students_attendance, view_attendance,student_view_routine,student_routine_today,view_result
urlpatterns = [
    path('sc',get_students_by_class),
    path('ss',get_subjects_by_student),
    path('students_attendance/<int:class_id>',students_attendance,name="students-attendance"),
    path('viewattendance/<int:class_id>',view_attendance,name="view-attendance"),
    path('edit_attendance/<int:attendance_id>/', edit_attendance, name='edit_attendance'),
    path('studentviewroutine/<int:class_id>',student_view_routine,name='student-view-routine'),
    path('studentroutinetoday/<int:class_id>',student_routine_today,name='student-today-routine'),
    path('viewresult/<int:student_id>',view_result,name='view_result'),
]
