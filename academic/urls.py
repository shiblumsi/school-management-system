from django.urls import path
from .views import   create_class_routine,view_class_routine,view_exam_routine,tution_fee,view_tution_fee
urlpatterns = [
    #path('viewclassroutine',class_routine,name="view-class-routine"),
    path('createclassroutine',create_class_routine,name="create-class-routine"),
    path('viewclassroutine/<int:class_id>',view_class_routine,name="view-class-routine"),
    path('viewexamroutine',view_exam_routine,name="view-exam-routine"),
    path('tution_fee/<int:student_id>',tution_fee,name="tution_fee"),
    path('view_tution_fee/<int:student_id>',view_tution_fee,name="view-tution_fee"),
]
