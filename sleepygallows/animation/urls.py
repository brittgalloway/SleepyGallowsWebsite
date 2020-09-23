"""
animation URL Configuration
"""
from django.urls import path

from . import views


urlpatterns = [
    path('/animation', include('animation.urls')),
    
]
