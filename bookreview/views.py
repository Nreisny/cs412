from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Book, Character, BookCommment, CharacterComment
from .forms import CreateCharacterCommentForm, CreateBookCommentForm

# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name = "bookreview/show_all_profiles.html"
    context_object_name = "profiles"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "bookreview/show_profile.html"
    context_object_name = "profile"

class BookListView(ListView):
    model = Book
    template_name = "bookreview/show_all_books.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "bookreview/show_book.html"
    context_object_name = "book"

class CharacterListView(ListView):
    model = Character
    template_name = "bookreview/show_all_characters.html"
    context_object_name = "characters"

class ChracterDetailView(DetailView):
    model = Character
    template_name = "bookreview/show_chracter.html"
    context_object_name = "character"

class CreateCharacterCommentView(CreateView):
    form_class = CreateCharacterCommentForm
    template_name = ""

    def form_valid(self, form):
        pk = self.kwargs["pk"]
        character = Character.objects.get(pk=pk)
        form.instance.character = character
        return super().form_valid(form)
    
class CreateBookCommentView(CreateView):
    form_class = CreateBookCommentForm
    template_name = ""

    def form_valid(self, form):
        pk = self.kwargs["pk"]
        book = Book.objects.get(pk=pk)
        form.instance.book = book
        return super().form_valid(form)
    

