from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class uploadfilemodel(models.Model):
    file = models.FileField(null = True)

    class Meta:
        db_table = "uploads"

class Post(models.Model):
    body = RichTextField(blank=True, null = True)

class User(models.Model): 
    #user id i think automatic na ma generate .. try
    username = models.CharField(max_length = 20, unique=True, null=False) #added unique 
    password = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 50, unique = True , null = False)
    