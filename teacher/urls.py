from django.urls import path
from .views import create_department,teacher_gives_mark,give_mark
urlpatterns = [
    path('createdepertment',create_department,name='create-depertment'),
    path('teachergivesmark',teacher_gives_mark,name='teacher-gives-mark'),
    path('givemark/<int:subject_id>',give_mark,name='give-mark'),
]