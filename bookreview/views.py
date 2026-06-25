# File: views.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: This is where we handle requests and process data to return to user

from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Book, Character, BookCommment, CharacterComment
from .forms import CreateCharacterCommentForm, CreateBookCommentForm, CreateProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class BookReviewLoginRequiredMixin(LoginRequiredMixin):
    """Require authentication before accessing a view."""

    def get_login_url(self):
        return reverse("login")

    def get_logged_in_profile(self):
        return Profile.objects.get(user=self.request.user)

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
    
class CreateCharacterCommentView(BookReviewLoginRequiredMixin, CreateView):
    '''Defines a view that displays a form for a creating a comment about a chracter'''
    form_class = CreateCharacterCommentForm
    template_name = "bookreview/create_character_comment_form.html"

    def form_valid(self, form):
        '''Where we connect a chracter to a comment foreign key'''
        pk = self.kwargs["pk"]
        character = Character.objects.get(pk=pk)
        form.instance.character = character

        form.instance.profile = self.get_logged_in_profile()

        # Adding the new rating to the characters rating and updating numratings
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

class CreateBookCommentView(BookReviewLoginRequiredMixin, CreateView):
    '''Defines a view that displays a form for creating a comment about a book'''
    form_class = CreateBookCommentForm
    template_name = "bookreview/create_book_comment_form.html"

    def form_valid(self, form):
        '''Where we connect a bok to a comments foreign key'''
        pk = self.kwargs["pk"]
        book = Book.objects.get(pk=pk)
        form.instance.book = book

        form.instance.profile = self.get_logged_in_profile()

        # Adding the new rating to the books rating and updating numratings
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

class CreateProfileView(CreateView):
    """Displays and processes the form used to create a Profile."""

    form_class = CreateProfileForm
    template_name = "bookreview/create_profile_form.html"

    def get_context_data(self, **kwargs):
        '''Adding the user creation form into the context'''
        context = super().get_context_data(**kwargs)
        context["user_form"] = UserCreationForm()
        return context

    def form_valid(self, form):
        '''Validating the form and adding the user to the profile fk'''

        user_form = UserCreationForm(self.request.POST)
        if not user_form.is_valid():
            return self.form_invalid(form)

        user = user_form.save()
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")
        form.instance.user = user

        return super().form_valid(form)

    def get_success_url(self):
        '''Sends the user to the profile page'''
        return reverse("my_profile")
    
class MyProfileDetailView(BookReviewLoginRequiredMixin, DetailView):
    """Display the logged-in user's profile."""

    model = Profile
    template_name = "bookreview/show_profile.html"
    context_object_name = "profile"

    def get_object(self):
        '''Returning the profile of the user logged in'''
        return self.get_logged_in_profile()