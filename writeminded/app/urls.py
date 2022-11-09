from cgitb import html
from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage, name = 'LandingPage'),
    path('About', views.About, name = 'About'),
    path('Signin', views.Signin, name = 'Signin'),
   
]


