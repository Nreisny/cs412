from django.shortcuts import render
from .models import Picture, Joke
from django.views.generic import DetailView, ListView
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