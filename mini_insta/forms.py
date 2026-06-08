# File: forms.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/2/26
# Description: Defines the forms used by the mini insta 

from django import forms
from .models import *

class CreateProfileForm(forms.ModelForm):
    '''Create a new Profile object'''

    class Meta:
        '''Associates this form with a model from our database'''

        model = Profile

        fields = [
            "username",
            "display_name",
            "bio_text",
            "profile_image_url"
        ]

class CreatePostForm(forms.ModelForm):
    '''A form to add a Post to the database'''

    class Meta:
        '''Associate this form with a model from our database'''
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a Profile to the database'''

    class Meta:
        '''Associates this form with a model from our database'''
        model = Profile
        fields = ['username', 'display_name', 'bio_text', 'profile_image_url']

class UpdatePostForm(forms.ModelForm):
    '''A form to update a Post to the database'''

    class Meta:
        model = Post
        fields = ['caption']