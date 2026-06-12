# File: Url.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/11/26
# Description: Our router for our views controller and our api endpoint

from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_view, name='home'),
    path('random/', views.random_view, name='random'),
    path('jokes/', views.JokeListView.as_view(), name='jokes'),
    path('joke/<int:pk>/', views.JokeDetailView.as_view(), name='joke'),
    path('pictures/', views.PictureListView.as_view(), name='pictures'),
    path('picture/<int:pk>/', views.PictureDetailView.as_view(), name='picture'),
    path('api/jokes', views.JokeListAPIView.as_view()),
    path('api/joke/<int:pk>', views.JokeDetailAPIView.as_view()),
    path('api/pictures', views.PictureListAPIView.as_view()),
    path('api/picture/<int:pk>', views.PictureDetailAPIView.as_view()),
]