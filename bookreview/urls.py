# File: urls.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/20/26
# Description: Our router for our views controller and our api endpoint

from django.urls import path, re_path
from django.conf import settings
from .views import *

urlpatterns = [
    path(r"", BookListView.as_view(), name="show_all_books"),
    path(r"book/<int:pk>/<path:previous_path>/", BookDetailView.as_view(), name="show_book"),
    path(r"book/<int:pk>/create_comment", CreateBookCommentView.as_view(), name="create_book_comment"),
    path(r"profile/show_all", ProfileListView.as_view(), name="show_all_profiles"),
    path(r"profile/<int:pk>", ProfileDetailView.as_view(), name="show_profile"),
    path(r"character/show_all", CharacterListView.as_view(), name="show_all_characters"),
    path(r"character/<int:pk>/<path:previous_path>", ChracterDetailView.as_view(), name="show_character"),
    path(r"character/<int:pk>/create_comment", CreateCharacterCommentView.as_view(), name="create_character_comment"),
]