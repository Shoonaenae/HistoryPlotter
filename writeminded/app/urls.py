from django.conf import settings
from django.conf.urls.static import static
from cgitb import html
from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage, name = 'LandingPage'),
    path('About', views.About, name = 'About'),

    path('Signin', views.SigninView.as_view(), name = 'Signin'),

    path('Signup', views.SignupView.as_view(), name = 'Signup'),

    path('LM_CreateChapter', views.LM_CreateChapter, name = 'LM_CreateChapter'),
    path('ProjectDashboard', views.ProjectDashboard, name = 'ProjectDashboard'),
    path('Relations', views.Relations, name = "Relations"),
    path('CreateQuiz', views.CreateQuiz, name = "CreateQuiz"),
    path('EditQuiz', views.EditQuiz, name = "EditQuiz"),
    path('ViewQuiz', views.ViewQuiz, name = "ViewQuiz"),
    path('ideaNest', views.ideaNest, name = "ideaNest"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)