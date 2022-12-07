from django.conf import settings
from django.conf.urls.static import static
from cgitb import html
from typing import ValuesView
from django.urls import path
from . import views
from .views import MaterialsView, MaterialDetailView, AddMaterialsView, UpdateMaterialDescriptionsView

urlpatterns = [
    path('ideanestdelete/<str:pk>', views.ideanestdelete, name = "ideanestdelete"),
    path('ideaNest', views.ideaNest, name = "ideaNest"),
    path('ideaNestEdit/<str:pk>', views.ideaNestEdit, name = "ideaNestEdit"),
    path('', views.LandingPage, name = 'LandingPage'),
    path('About', views.About, name = 'About'),

    path('Signin', views.SigninView.as_view(), name = 'Signin'),

    path('Signup', views.SignupView.as_view(), name = 'Signup'),


    path('ProjectDashboard', views.ProjectDashboard, name = 'ProjectDashboard'),
    path('Relations', views.Relations, name = "Relations"),
    path('CreateQuiz', views.CreateQuizView.as_view(), name = "CreateQuiz"),
    path('EditQuiz', views.EditQuizView.as_view(), name = "EditQuiz"),
    path('ViewQuiz', views.ViewQuiz, name = "ViewQuiz"),

    path('Quiz', views.QuizView.as_view(), name = "Quiz"),

    path('', MaterialsView.as_view(), name="materials"),
    path('materials/<int:pk>', MaterialDetailView.as_view(), name="material-details"),
    #pk->primary key... unique id number assigned to new database record entry
    path('add_material/', AddMaterialsView.as_view(), name = 'add-materials'),
    path('material/edit/<int:pk>', UpdateMaterialDescriptionsView.as_view(), name = 'update-materials')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)