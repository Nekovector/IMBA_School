from django.urls import path
from . import views

urlpatterns = [
    path('', views.directions, name='courses_home'),
    path('entry-form', views.entryForm, name='passport')
]
