from django.urls import path
from .views import create_department
urlpatterns = [
    path('createdepertment',create_department,name='create-depertment'),
]