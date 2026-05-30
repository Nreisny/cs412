# File: models.py
# Author: Nicholas Reis (nreisny@bu.edu) 5/28/26
# Description: Defines the Profile model used by the Mini Insta application.

from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Represents a Mini Insta user profile'''
    username = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''String representation of this model'''
        return f"User: {self.username}"
    
    def get_all_posts(self):
        '''Returns all posts that are connected to this Profile'''
        posts = Post.objects.filter(profile=self)
        return posts

    
class Post(models.Model):
    '''Represents a Mini Insta user Post'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''String representation of this Post model'''
        return f"Profile: {self.profile}"
    
    def get_all_photos(self):
        '''Returns all Photo's that are connected to this Post'''
        photos = Photo.objects.filter(post=self)
        return photos

    def get_first_photo(self):
        '''Returns the first photo that is connected to this Post'''
        photos = Photo.objects.first()
        return photos

class Photo(models.Model):
    '''Represents a Mini Insta user Photo'''
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

