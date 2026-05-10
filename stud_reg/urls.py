from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.home1, name='home1'),
    path('studentlist/', views.studentlist, name='studentlist'),
    path('courselist/', views.courselist, name='courselist'),
    path('register/', views.register, name='register'),
    path('enrolledlist/', views.enrolledStudents, name='enrolledStudents'),
]