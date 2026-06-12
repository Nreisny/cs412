# File: Url.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/11/26
# Description: Our router for our views controller and our api endpoint

from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.random_view, name='home'),
    path(r'random/', views.random_view, name='random'),
    path(r'jokes/', views.JokeListView.as_view(), name='jokes'),
    path(r'joke/<int:pk>/', views.JokeDetailView.as_view(), name='joke'),
    path(r'pictures/', views.PictureListView.as_view(), name='pictures'),
    path(r'picture/<int:pk>/', views.PictureDetailView.as_view(), name='picture'),
    path(r'api/jokes', views.JokeListAPIView.as_view()),
    path(r'api/joke/<int:pk>', views.JokeDetailAPIView.as_view()),
    path(r'api/pictures', views.PictureListAPIView.as_view()),
    path(r'api/picture/<int:pk>', views.PictureDetailAPIView.as_view()),
    path(r'api/random_picture', views.RandomPictureDetailView.as_view()),
    path(r'api/random', views.RandomJokeDetailAPIVeiw.as_view()),
    path(r'api/', views.RandomJokeDetailAPIVeiw.as_view()),
]