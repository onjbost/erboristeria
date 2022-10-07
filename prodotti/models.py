from distutils.command.upload import upload
from turtle import right
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank = True, null=True)
    modo_uso = models.TextField(blank=True, null= True)
    ingredienti = models.TextField(blank=True, null=True)
    price = models.FloatField()
    capacity = models.TextField(max_length=100)
    front_image = models.ImageField(upload_to='images/', null=True, blank = True)
    left_image = models.ImageField(upload_to='images/', null=True, blank = True)
    back_image = models.ImageField(upload_to='images/', null=True, blank = True)

    
    def __str__(self):
        return self.name
    

    
    