from django.shortcuts import render
from .models import Picture, Joke
from django.views.generic import DetailView, ListView
from rest_framework import generics
from .serializers import *
import random
# Create your views here.

def random_view(request):
    joke = random.choice(Joke.objects.all())
    picture = random.choice(Picture.objects.all())

    context = {
        'joke': joke,
        'picture': picture,
    }

    return render(request, 'dadjokes/show_random.html', context)

class JokeListView(ListView):
    model = Joke
    template_name = 'dadjokes/show_all_jokes.html'
    context_object_name = 'jokes'


class JokeDetailView(DetailView):
    model = Joke
    template_name = 'dadjokes/show_joke.html'
    context_object_name="joke"


class PictureListView(ListView):
    model = Picture
    template_name = 'dadjokes/show_all_pictures.html'
    context_object_name = 'pictures'


class PictureDetailView(DetailView):
    model = Picture
    template_name = 'dadjokes/show_picture.html'
    context_object_name = 'picture'

class JokeListAPIView(generics.ListCreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class PictureListAPIView(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class RandomJokeDetailAPIVeiw(generics.RetrieveAPIView):
    serializer_class = JokeSerializer

    def get_queryset(self):
        all_jokes = Joke.objects.all()
        n = random.randint(0, len(all_jokes))
        return all_jokes[n]

class RandomPictureDetailView(generics.RetrieveAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        all_pictures = Picture.objects.all()
        n = random.randint(0, len(all_pictures))
        return all_pictures[n]

