# File: views.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: This is where we handle requests and process data to return to user

from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Book, Character, BookCommment, CharacterComment
from .forms import CreateCharacterCommentForm, CreateBookCommentForm

# Create your views here.

class ProfileListView(ListView):
    '''Defines a view that displays a list of profiles'''
    model = Profile
    template_name = "bookreview/show_all_profiles.html"
    context_object_name = "profiles"


class ProfileDetailView(DetailView):
    '''Defiens a view that displays a profile'''
    model = Profile
    template_name = "bookreview/show_profile.html"
    context_object_name = "profile"

class BookListView(ListView):
    '''Defines a view that displays a list of books'''
    model = Book
    template_name = "bookreview/show_all_books.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    '''Defines a view that displays a book'''
    model = Book
    template_name = "bookreview/show_book.html"
    context_object_name = "book"

class CharacterListView(ListView):
    '''Defines a view that displays a list of characters'''
    model = Character
    template_name = "bookreview/show_all_characters.html"
    context_object_name = "characters"

class ChracterDetailView(DetailView):
    '''Defines a view that displays a character'''
    model = Character
    template_name = "bookreview/show_character.html"
    context_object_name = "character"

class CreateCharacterCommentView(CreateView):
    '''Defines a view that displays a form for a creating a comment about a chracter'''
    form_class = CreateCharacterCommentForm
    template_name = "bookreview/create_character_comment_form.html"

    def form_valid(self, form):
        '''Where we connect a chracter to a comment foreign key'''
        pk = self.kwargs["pk"]
        character = Character.objects.get(pk=pk)
        form.instance.character = character

        character.rating = (((character.rating * character.numrating) + form.instance.rating) / (character.numrating + 1))
        character.numrating += 1
        character.save()

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        '''Adding in the character object into the context for access in template'''
        context = super().get_context_data(**kwargs)
        context["character"] = Character.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        '''Sends the user to the character page for the character they wrote the comment for'''
        return reverse("show_character", kwargs={"pk": self.kwargs["pk"]})
        

class CreateBookCommentView(CreateView):
    '''Defines a view that displays a form for creating a comment about a book'''
    form_class = CreateBookCommentForm
    template_name = "bookreview/create_book_comment_form.html"

    def form_valid(self, form):
        '''Where we connect a bok to a comments foreign key'''
        pk = self.kwargs["pk"]
        book = Book.objects.get(pk=pk)
        form.instance.book = book

        book.rating = (((book.rating * book.numrating) + form.instance.rating) / (book.numrating + 1))
        book.numrating += 1
        book.save()

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        '''Adding in the book object into the context for access in template'''
        context = super().get_context_data(**kwargs)
        context["book"] = Book.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        '''Sends the user to the book page for the book they wrote the comment for'''
        return reverse("show_book", kwargs={"pk": self.kwargs["pk"]})
    

