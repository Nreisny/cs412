# File: views.py
# Author: Nicholas Reis (nreisny@bu.edu) 5/30/26
# Description: Defines views for displaying Mini Insta profiles.

from .models import Profile, Post, Photo
from django.views.generic import ListView, DetailView, CreateView
from .forms import CreatePostForm

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

class PostDetailView(DetailView):
    '''Defines a class to view all Posts'''
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self):
        '''Return the dictionary of context varaibles for use in the template'''

        context = super().get_context_data()

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        '''This method handles the form submission and the saving of it into the database'''

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile
        response = super().form_valid(form)

        # We are creating the photo object here
        files = self.request.FILES.getlist('image_file')
        for file in files:
            Photo.objects.create(
                post=self.object,
                image_file=file
            )

        return response
    