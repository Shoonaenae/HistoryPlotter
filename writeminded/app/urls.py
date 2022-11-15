from cgitb import html
from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('LandingPage', views.LandingPage, name = 'LandingPage'),
    path('About', views.About, name = 'About'),
    path('Signin', views.Signin, name = 'Signin'),
    path('Signup', views.Signup, name = 'Signup'),
    path('LM_CreateChapter', views.LM_CreateChapter, name = 'LM_CreateChapter'),
    path('ProjectDashboard', views.ProjectDashboard, name = 'ProjectDashboard'),
    path('Relations', views.Relations, name = "Relations"),
    path('CreateQuiz', views.CreateQuiz, name = "CreateQuiz"),
    path('EditQuiz', views.EditQuiz, name = "EditQuiz"),
    path('ViewQuiz', views.ViewQuiz, name = "ViewQuiz"),
    
]


