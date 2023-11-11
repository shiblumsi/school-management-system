from django.urls import path
from .views import create_department, get_highest_mark,teacher_gives_mark,give_mark,teacher_login,teacher_deshboard,edit_mark, view_mark
urlpatterns = [
    path('teacher_login',teacher_login,name='teacher-login'),
    path('teacher_deshboard',teacher_deshboard,name='teacher-deshboard'),

    path('createdepertment',create_department,name='create-depertment'),
    path('teachergivesmark',teacher_gives_mark,name='teacher-gives-mark'),
    path('givemark/<int:subject_id>',give_mark,name='give-mark'),
    path('viewmark/<int:subject_id>',view_mark,name='view-mark'),
    path('editmark/<int:mark_id>',edit_mark,name='edit-mark'),
    
    path('get_highest_mark/<int:subject_id>',get_highest_mark,name='get-highest-mark'),
]