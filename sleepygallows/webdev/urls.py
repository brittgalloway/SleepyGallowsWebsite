"""
webdev URL Configuration
"""
from django.urls import path

from . import views


urlpatterns = [
    path('/webdev', include('animation.urls')),

    
]
