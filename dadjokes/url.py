from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_view, name='home'),
    path('random/', views.random_view, name='random'),
    path('jokes/', views.JokeListView.as_view(), name='jokes'),
    path('joke/<int:pk>/', views.JokeDetailView.as_view(), name='joke'),
    path('pictures/', views.PictureListView.as_view(), name='pictures'),
    path('picture/<int:pk>/', views.PictureDetailView.as_view(), name='picture'),
]