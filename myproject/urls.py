"""
URL configuration for myproject project.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('placeholder', views.placeholder, name='placeholder'),
]
