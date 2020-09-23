"""
animation URL Configuration
"""
from django.urls import path

from . import views


urlpatterns = [
    path('/animation', views.index, name=index),
    path('/animation/client', views.client, name=client),
    path('/animation/original', views.original, name=original),
    path('/animation/original/plh', views.plh, name=plh),
    path('/animation/fun', views.fun, name=fun),
    
]
