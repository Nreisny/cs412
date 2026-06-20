from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path(r"", BookListView.as_view(), name="show_all_books"),
    path(r"book/<int:pk>", BookDetailView.as_view(), name="show_book"),
    path(r"profile/show_all", ProfileListView.as_view(), name="show_all_profiles"),
    path(r"profile/<int:pk>", ProfileDetailView.as_view(), name="show_profile"),
    path(r"character/show_all", CharacterListView.as_view(), name="show_all_characters"),
    path(r"character/<int:pk>", ChracterDetailView.as_view(), name="show_character"),
]