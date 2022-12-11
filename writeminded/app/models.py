from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class uploadfilemodel(models.Model):
    filename = models.CharField(max_length=20, unique=True, null=True)
    description = models.CharField(max_length=50, null=True)
    file = models.FileField(null = True)

    class Meta:
        db_table = "filesUploaded"

class Post(models.Model):
    body = RichTextField(blank=True, null = True)

class User(models.Model): 
    #user id i think automatic na ma generate .. try
    username = models.CharField(max_length = 20, unique=True, null=False) #added unique 
    password = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 50, unique = True , null = False)

# quiz
class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quiz_name = models.CharField(max_length=100)
    quiz_desc = models.TextField(default=None)
    quiz_date = models.DateField(blank=True)
    #quiz_type = models.CharField(max_length=50)

class QuizRepo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete= models.CASCADE)
    q_num = models.IntegerField()
    question = models.CharField(max_length=500)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    answer = models.CharField(max_length= 100)
    isAnswer = models.BooleanField(default=False)
# end quiz

class Materials(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('material-details', args=(str(self.id)))

# Project
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
