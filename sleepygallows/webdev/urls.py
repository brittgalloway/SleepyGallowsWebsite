"""
webdev URL Configuration
"""
from django.urls import path

from . import views


urlpatterns = [
    path('/webdev', include('webdev.urls')),
    path('<int:project_id>/',views.project, include('webdev.urls')),
    
]
