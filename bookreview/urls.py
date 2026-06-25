# File: urls.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: Our router for our views controller and our api endpoint

from django.urls import path, re_path
from django.conf import settings
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r"", BookListView.as_view(), name="show_all_books"),
    path(r"book/<int:pk>/<path:previous_path>/", BookDetailView.as_view(), name="show_book"),
    path(r"book/<int:pk>/<path:previous_path>/create_comment", CreateBookCommentView.as_view(), name="create_book_comment"),
    path(r"profile/show_all", ProfileListView.as_view(), name="show_all_profiles"),
    path(r"profile/<int:pk>/<path:previous_path>", ProfileDetailView.as_view(), name="show_profile"),
    path(r"character/show_all", CharacterListView.as_view(), name="show_all_characters"),
    path(r"character/<int:pk>/<path:previous_path>", ChracterDetailView.as_view(), name="show_character"),
    path(r"character/<int:pk>/<path:previous_path>/create_comment", CreateCharacterCommentView.as_view(), name="create_character_comment"),
    path("profile", MyProfileDetailView.as_view(), name="my_profile"),
    path("login", auth_views.LoginView.as_view(template_name="bookreview/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(next_page="show_all_books"), name="logout"),
    path("create_profile/", CreateProfileView.as_view(), name="create_profile"),
]