# File: models.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/11/26
# Description: Defines a model that represents a Joke and Picture
#              object from our database

from django.db import models

# Create your models here.
class Joke(models.Model):
    joke = models.TextField(blank=True)
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)

class Picture(models.Model):
    image_url = models.URLField(blank=True)
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)
