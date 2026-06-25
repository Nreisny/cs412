# File: urls.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: Our router for our views controller and our api endpoint

from django.urls import path, re_path
from django.conf import settings
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", BookListView.as_view(), name="show_all_books"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="show_book"),
    path("book/<int:pk>/create_comment", CreateBookCommentView.as_view(), name="create_book_comment"),
    path("profile/show_all", ProfileListView.as_view(), name="show_all_profiles"),
    path("profile/<int:pk>", ProfileDetailView.as_view(), name="show_profile"),
    path("character/show_all", CharacterListView.as_view(), name="show_all_characters"),
    path("character/<int:pk>", ChracterDetailView.as_view(), name="show_character"),
    path("character/<int:pk>/create_comment", CreateCharacterCommentView.as_view(), name="create_character_comment"),
    path("profile", MyProfileDetailView.as_view(), name="my_profile"),
    path("login", auth_views.LoginView.as_view(template_name="bookreview/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(next_page="show_all_books"), name="logout"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),
]