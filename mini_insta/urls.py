# File: urls.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/2/26
# Description: URL patterns for the Mini Insta application.

from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

# Adding paths to Mini_insta
urlpatterns = [
 path(r"", views.ProfileListView.as_view(), name="show_all_profile"),
 path(r"profile/<int:pk>", views.ProfileDetailView.as_view(), name="show_profile"),
 path(r"post/<int:pk>", views.PostDetailView.as_view(), name="show_post"),
 path(r"profile/create_post", views.CreatePostView.as_view(), name="create_post"),
 path(r"profile/update_profile", views.UpdateProfileView.as_view(), name="update_profile"),
 path(r"delete_post/<int:pk>", views.DeletePostView.as_view(), name="delete_post"),
 path(r"update_post/<int:pk>", views.UpdatePostView.as_view(), name="update_post"),
 path(r"profile/<int:pk>/followers", views.ShowFollowersDetailVew.as_view(), name="show_followers"),
 path(r"profile/<int:pk>/following", views.ShowFollowingDetailView.as_view(), name="show_following"),
 path(r"profile/feed", views.ShowFeedView.as_view(), name='show_feed'),
 path(r"profile/search", views.SearchView.as_view(), name='search'),
 path(r"profile", views.MyProfileView.as_view(), name="my_profile"),
 path(r"login/", auth_views.LoginView.as_view(template_name="mini_insta/login.html"), name="login"),
 path(r"logout/", auth_views.LogoutView.as_view(next_page="logout_confirmation"), name="logout"),
 path(r"logout_confirmation/", views.LogoutConfirmationView.as_view(), name="logout_confirmation"),
 path(r"create_profile", views.CreateProfileView.as_view(), name="create_profile"),
 path(r"profile/<int:pk>/follow", views.CreateFollowView.as_view(), name="follow"),
 path(r"profile/<int:pk>/delete_follow", views.DeleteFollowView.as_view(), name="delete_follow"),
 path(r"post/<int:pk>/like", views.CreateLikeView.as_view(), name="like"),
 path(r"post/<int:pk>/delete_like", views.DeleteLikeView.as_view(), name="delete_like"),
]