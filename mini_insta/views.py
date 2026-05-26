from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView, DetailView
# Create your views here.
class ProfileListView(ListView):
    '''Defines a class to view all profiles'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''Defines a class to view a single profile'''
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"