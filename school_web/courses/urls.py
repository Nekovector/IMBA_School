from django.urls import path
from . import views

urlpatterns = [
    path('', views.directions, name='courses_home'),
    path('entry-form', views.entryForm, name='passport'),
    path('improving_academic_performance', views.grade_info, name='grade_info')
]
