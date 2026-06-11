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
