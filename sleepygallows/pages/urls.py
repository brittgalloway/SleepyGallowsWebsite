"""
page URL Configuration
"""
from django.urls import include, path

from . import views


urlpatterns = [
    path('', include('page.urls')),
    path('/about', include('page.urls')),
    path('/comics', include('page.urls')),
    
]