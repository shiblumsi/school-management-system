from django.urls import path
from .views import   create_class_routine
urlpatterns = [
    #path('viewclassroutine',class_routine,name="view-class-routine"),
    path('createclassroutine',create_class_routine,name="create-class-routine"),
]
