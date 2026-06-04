# File: views.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/2/26
# Description: Defines views for displaying Mini Insta profiles.

from .models import Profile, Post, Photo, Follow
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class UpdateProfileView(UpdateView):
    '''A view to update a Profile and save it to the database'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def form_valid(self, form):
        '''Handles the form submission to create a new Profile object'''
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')

        return super().form_valid(form)
    
class DeletePostView(DeleteView):
    '''A view to delete a post and remove it from the database'''
    model = Post
    template_name = "mini_insta/delete_post_form.html"
    content_object_name = "post"

    def get_success_url(self):
        '''Rerouting the user to their profile page after deleting a post'''
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        Profile = post.profile

        return reverse("show_profile", kwargs={"pk": Profile.pk})
    
class UpdatePostView(UpdateView):
    '''A view to udpdate a post and save it to the database'''
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def form_valid(self, form):
        '''Handles the form submission to create a new Profile object'''
        print(f'UpdatePostForm: form.cleaned_data={form.cleaned_data}')

        return super().form_valid(form)
    
class ShowFollowersDetailVew(DetailView):
    '''Defines a class to view a single profiles followers list'''
    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "followers"

class ShowFollowingDetailView(DetailView):
    '''Defines a class to view a single profiles following list'''
    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = "following"
