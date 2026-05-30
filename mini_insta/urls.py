# File: urls.py
# Author: Nicholas Reis (nreisny@bu.edu) 5/28/26
# Description: URL patterns for the Mini Insta application.

from django.urls import path
from django.conf import settings
from . import views

# Adding paths to Mini_insta
urlpatterns = [
 path(r"", views.ProfileListView.as_view(), name="show_all_profile"),
 path(r"profile/<int:pk>", views.ProfileDetailView.as_view(), name="show_profile"),
 path(r"post/<int:pk>", views.PostDetailView.as_view(), name="show_post"),
 path(r"profile/<int:pk>/create_post", views.CreatePostView.as_view(), name="create_post")
]