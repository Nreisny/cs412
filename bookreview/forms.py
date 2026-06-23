# File: forms.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: This file simply imforms django what model and fields should
#              be used when creating a form

from django import forms
from .models import *

class CreateCharacterCommentForm(forms.ModelForm):
    '''Create a new Character Comment object'''
    class Meta:
        '''Associates this form with a model from our database'''
        model = CharacterComment
        fields = ["profile", "text", "rating"]

class CreateBookCommentForm(forms.ModelForm):
    '''Create a new Book Comment object'''
    class Meta:
        '''Associates this form with a model from our database'''
        model =  BookCommment
        fields = ["profile", "text", "rating"]