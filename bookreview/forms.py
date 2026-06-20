from django import forms
from .models import *

class CreateCharacterCommentForm(forms.ModelForm):
    class Meta:
        model = CharacterComment
        fields = ["profile", "text"]

class CreateBookCommentForm(forms.ModelForm):
    class Meta:
        model =  BookCommment
        fields = ["profile", "text"]