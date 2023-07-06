from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('online-school', views.online_info, name='online_info')
]
