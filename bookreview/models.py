# File: models.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: This file basically structures the data
#              that is used to map to a database table

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    '''Represents a bookreview user profile'''
    username = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookreview_profiles", null=True, blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''String reperesentation of a Profile Model'''
        return f"User: {self.username}"
    
    def get_all_book_comments(self):
        '''Retruns a query set of all book comments made by this profile'''
        return BookCommment.objects.filter(profile=self)
    
    def get_all_character_comments(self):
        '''Retruns a query set of all character comments made by this profile'''
        return CharacterComment.objects.filter(profile=self)

class Book(models.Model):
    '''Represents a bookreview book'''
    name = models.CharField(max_length=200)
    book_image_url = models.URLField(blank=True)
    synopsis = models.TextField(blank=True)
    author = models.CharField(max_length=60)
    rating = models.FloatField(blank=True)
    numrating = models.IntegerField(blank=True)

    def __str__(self):
        '''String reperesentation of a Book Model'''
        return f"Book Name: {self.name}"
    
    def get_all_comments(self):
        '''Returns a query set of all comments about this book'''
        return BookCommment.objects.filter(book=self)
    
    def get_all_characters(self):
        '''Returns a query set of all characters in this book'''
        return Character.objects.filter(book=self)
    
class Character(models.Model):
    '''Represents a bookreview character'''
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    rating = models.FloatField(blank=True)
    numrating = models.IntegerField(blank=True)

    def __str__(self):
        '''String representation of a Character Model'''
        return f"Character Name: {self.name}"
    
    def get_all_comments(self):
        '''Returns a query set of all comments about this character'''
        return CharacterComment.objects.filter(character=self)
    
class BookCommment(models.Model):
    '''Represents a bookreview book comment'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    rating = models.FloatField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        '''String representation of a BookComment Model'''
        return f"{self.profile.username}: {self.text}"
    
class CharacterComment(models.Model):
    '''Represents a bookreview character comment'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    rating = models.FloatField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        '''String representation of a CharacterComment Model'''
        return f"{self.profile.username}: {self.text}"

