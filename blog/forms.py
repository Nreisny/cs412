from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):
    '''A form to add an Article to the database'''

    class Meta:
        '''Associate this form with a model from our database'''
        model = Article
        fields = ['author', 'title', 'text', 'image_file']

class CreateCommentForm(forms.ModelForm):
    '''A form to add a comment to the database'''

    class Meta:
        '''Associates this form with a model from our database'''
        model = Comment
        #fields = ['article', 'author', 'text']
        fields = ['author', 'text'] # we dont want the drop-down list so doing this instead