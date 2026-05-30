# File: forms.py
# Author: Nicholas Reis (nreisny@bu.edu) 5/30/26
# Description: Defines the forms used by the mini insta application

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to add a Post to the database'''

    class Meta:
        '''Associate this form with a model from our database'''
        model = Post
        fields = ['caption']