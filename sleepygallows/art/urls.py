"""
art URL Configuration
"""
from django.urls import path

from . import views

app_name = 'art'
urlpatterns = [
    path('/art', views.index, name=index),
    path('/art/brittney', views.brittney, name=brittney),
    path('/art/brittney/sketchbook', views.sketchbook, name=sketchbook),
    path('/art/brittney/papercuts', views.papercuts, name=papercuts),
    path('/art/crystal', views.crystal, name=crystal),
    path('/art/crystal/illustration', views.illustration, name=illustration),
    path('/art/crystal/visdev', views.visdev, name=visdev),

]