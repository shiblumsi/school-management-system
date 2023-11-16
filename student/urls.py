from django.urls import path
from .views import add_student,about_student,all_students, edit_student,students_list,edit_attendance, aa, get_subjects_by_student, student_login, student_profile, student_view_all_attendance, student_view_attendance, students_attendance, update_student_profile, view_attendance,student_view_routine,student_routine_today,view_result,student_deshboard

urlpatterns = [
    path('aa',aa),
    path('add_student',add_student,name='add-student'),
    path('all-students',all_students,name='all-students'),
    path('students_list',students_list,name='students-list'),
    path('edit-student',edit_student,name='edit-student'),
    path('about_student',about_student,name='about-student'),
    path('student_profile/<int:student_id>',student_profile,name='student-profile'),




    path('studentdeshboard',student_deshboard,name='student-deshboard'),
    path('studentlogin',student_login,name='student-login'),
    path('updatestudentprofile/<int:student_id>',update_student_profile,name='update-student-profile'),
    path('studentviewattendance/<int:student_id>',student_view_attendance,name='student-view-attendance'),
    path('studentviewallattendance/<int:student_id>',student_view_all_attendance,name='student-view-all-attendance'),
    path('students_attendance/<int:class_id>',students_attendance,name="students-attendance"),
    path('viewattendance/<int:class_id>',view_attendance,name="view-attendance"),
    path('edit_attendance/<int:attendance_id>/', edit_attendance, name='edit_attendance'),
    path('studentviewroutine/<int:class_id>',student_view_routine,name='student-view-routine'),
    path('studentroutinetoday/<int:class_id>',student_routine_today,name='student-today-routine'),
    path('viewresult/<int:student_id>',view_result,name='view_result'),
]
