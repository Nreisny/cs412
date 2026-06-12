# File: views.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/11/26
# Description: Defines a view class to act as a view controller
#              and an API endpoint

from django.shortcuts import render
from .models import Picture, Joke
from django.views.generic import DetailView, ListView
from rest_framework import generics
from .serializers import *
import random
# Create your views here.

def random_view(request):
    '''Defines a view that displays a random joke and a random picture'''
    joke = random.choice(Joke.objects.all())
    picture = random.choice(Picture.objects.all())

    context = {
        'joke': joke,
        'picture': picture,
    }

    return render(request, 'dadjokes/show_random.html', context)

class JokeListView(ListView):
    '''Defines a view that displays a list of all jokes'''
    model = Joke
    template_name = 'dadjokes/show_all_jokes.html'
    context_object_name = 'jokes'


class JokeDetailView(DetailView):
    '''Defines a view that displays a joke'''
    model = Joke
    template_name = 'dadjokes/show_joke.html'
    context_object_name="joke"


class PictureListView(ListView):
    '''Defines a view that dispalys a list of all pictures'''
    model = Picture
    template_name = 'dadjokes/show_all_pictures.html'
    context_object_name = 'pictures'


class PictureDetailView(DetailView):
    '''Defiens a view that displays a picture'''
    model = Picture
    template_name = 'dadjokes/show_picture.html'
    context_object_name = 'picture'

class JokeListAPIView(generics.ListCreateAPIView):
    '''List all jokes or create a new joke.'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update, or delete a specific joke.'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class PictureListAPIView(generics.ListCreateAPIView):
    '''List all pictures or create a new picture.'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update, or delete a specific picture.'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
