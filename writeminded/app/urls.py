from django.conf import settings
from django.conf.urls.static import static
from cgitb import html
from typing import ValuesView
from django.urls import path
from . import views
from .views import  MaterialsView, MaterialDetailView, AddMaterialsView, UpdateMaterialDescriptionsView, DeleteMaterialDescriptionView

urlpatterns = [
    path('ungroup/<str:pk>', views.ungroup, name = "ungroup"),
    path('editgroup/<str:pk>', views.editgroup.as_view(), name = "editgroup"),
    path('group', views.groupfiles.as_view(), name = "group"),
    path('ideanestdelete/<str:pk>', views.ideanestdelete, name = "ideanestdelete"),
    path('ideaNestEdit/<int:pk>', views.ideaNestEdit.as_view(), name = "ideaNestEdit"),
    path('ideaNest', views.ideaNest.as_view(), name = "ideaNest"),

    path('', views.LandingPageView.as_view(), name = 'LandingPage'),
    path('About', views.AboutView.as_view(), name = 'About'),

    path('Signin', views.SigninView.as_view(), name = 'Signin'),

    path('Signup', views.SignupView.as_view(), name = 'Signup'),


    path('ProjectDashboard', views.ProjectDashboard.as_view(), name = 'ProjectDashboard'),
    path('ProjectView ', views.ProjectView.as_view(), name = "ProjectView"),
    path('Relations', views.Relation.as_view(), name = "Relations"),

    path('CreateQuiz', views.CreateQuizView.as_view(), name = "CreateQuiz"),
    path('CreateQuiz/EditQuiz/', views.EditQuizView.as_view(), name = "EditQuiz"),

    #path('EditQuizOptions/<int:question_id>', views.EditQuizOptions, name = "EditQuizOptions"),
    path('EditQuizOptions/<int:question_id>', views.EditQuizOptionsView.as_view(), name = "EditQuizOptions"),
    #path('CreateQuiz/EditQuiz/EditQuizOptions/(?<question_id>\d+)/$', views.EditQuizOptionsView.as_view(), name = "EditQuizOptions"),

    path('CreateQuiz/EditQuiz/EditQuizOptions/Quiz', views.QuizView.as_view(), name = "Quiz"),

    path('write/', MaterialsView.as_view(), name="materials"),
    path('materials/<int:pk>', MaterialDetailView.as_view(), name="material-details"),
    #pk->primary key... unique id number assigned to new database record entry
    path('add_material/', AddMaterialsView.as_view(), name = 'add-materials'),
    path('material/edit/<int:pk>', UpdateMaterialDescriptionsView.as_view(), name = 'update-material'),
    path('material/<int:pk>/delete', DeleteMaterialDescriptionView.as_view(), name = 'delete-material'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)