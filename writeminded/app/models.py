from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import os
import datetime

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().old_filename('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)

    return os.path.join('uploads/', filename)

class Post(models.Model):
    body = RichTextField(blank=True, null = True)

class User(models.Model): 
    #user id i think automatic na ma generate .. try
    username = models.CharField(max_length = 20, unique=True, null=False) #added unique 
    password = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 50, unique = True , null = False)

class uploadfilemodel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=20, unique=True, null=True)
    description = models.CharField(max_length=50, null=True)
    file = models.FileField(null = True)
    cover = models.ImageField(null = True)

    class Meta:
        db_table = "uploadfile"

class groupmodel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ideafile = models.CharField(max_length=200, unique=True, null=True)
    name = models.CharField(max_length=20, unique=True, null=True)

    class Meta:
        db_table = "groupfiles"

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
    period = models.CharField(max_length=100, null=True)
    description = models.TextField()
    actual_material = RichTextField(blank=True, null=True)  


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('material-details', args=(str(self.id)))

# Project
class Project(models.Model):
    ideafile = models.ForeignKey(uploadfilemodel, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)