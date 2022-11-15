from ckeditor.fields import RichTextField
from django.db import models

#test push
# Create your models here.
class Post(models.Model):
    body = RichTextField(blank=True, null = True)