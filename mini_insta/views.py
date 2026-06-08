# File: views.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/2/26
# Description: Defines views for displaying Mini Insta profiles.

from .models import Profile, Post, Photo, Follow, Like
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm, CreateProfileForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

class InstaLoginRequiredMixin(LoginRequiredMixin):
    """Require authentication before accessing a view."""

    def get_login_url(self):
        """Return the URL required for user authentication."""
        return reverse('login')

    def get_logged_in_profile(self):
        """Return the Profile associated with the authenticated User."""

        return Profile.objects.get(user=self.request.user)
    
class MyProfileView(InstaLoginRequiredMixin, DetailView):
    """Display the Profile associated with the logged in User."""

    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

    def get_object(self):
        """Return the Profile associated with the authenticated User."""

        return Profile.objects.get(user=self.request.user)

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

    def get_context_data(self, **kwargs):
        '''Adding follow information to the context'''

        context = super().get_context_data(**kwargs)

        # Checking to see if user is authenticated then adding 
        # follow object with relationship to this profile to the context
        if self.request.user.is_authenticated:
            current_profile = Profile.objects.get(user=self.request.user)
            context["is_following"] = Follow.objects.filter(follower_profile=current_profile, profile=self.object).exists()

        return context

class PostDetailView(DetailView):
    '''Defines a class to view all Posts'''
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        '''Add like information to the context'''
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            current_profile = Profile.objects.get(user=self.request.user)
            context["has_liked"] = Like.objects.filter(profile=current_profile, post=self.object).exists()

        return context

class CreatePostView(InstaLoginRequiredMixin, CreateView):
    '''A View that handles the creation of a Post'''
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self):
        '''Return the dictionary of context varaibles for use in the template'''

        context = super().get_context_data()

        # Retrieving the Profile using the get_logged_in_profile method
        profile = self.get_logged_in_profile()

        # Adding the profile to the templates context
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        '''This method handles the form submission and the saving of it into the database'''

        profile = self.get_logged_in_profile()
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
    
    def get_success_url(self):
        '''This method sends the user back to their profile after verifying a form'''
        profile = self.get_logged_in_profile()

        return reverse('show_profile', kwargs={'pk': profile.pk})
    
class UpdateProfileView(InstaLoginRequiredMixin, UpdateView):
    '''A view to update a Profile and save it to the database'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def form_valid(self, form):
        '''Handles the form submission to create a new Profile object'''
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')

        return super().form_valid(form)
    
    def get_object(self):
        """Return the Profile associated with the authenticated User."""
        return self.get_logged_in_profile()

    def get_success_url(self):
        '''Rerouting the user to show their profile after updating it'''
        profile = self.get_logged_in_profile()
        return reverse('show_profile', kwargs={'pk': profile.pk})
    
class DeletePostView(InstaLoginRequiredMixin, DeleteView):
    '''A view to delete a post and remove it from the database'''
    model = Post
    template_name = "mini_insta/delete_post_form.html"
    content_object_name = "post"

    def get_success_url(self):
        '''Rerouting the user to their profile page after deleting a post'''

        # Grabbing the private key and finding the profile associated it
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        Profile = post.profile

        return reverse("show_profile", kwargs={"pk": Profile.pk})
    
class UpdatePostView(InstaLoginRequiredMixin, UpdateView):
    '''A view to udpdate a post and save it to the database'''
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def form_valid(self, form):
        '''Handles the form submission to create a new Profile object'''
        print(f'UpdatePostForm: form.cleaned_data={form.cleaned_data}')

        return super().form_valid(form)
    
    def get_success_url(self):
        '''Rerouting the user after updating a post back to the post'''
        return reverse('show_post', kwargs={'pk': self.kwargs['pk']})
    
class ShowFollowersDetailVew(DetailView):
    '''Defines a class to view a single profiles followers list'''
    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "profile"

class ShowFollowingDetailView(DetailView):
    '''Defines a class to view a single profiles following list'''
    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = "profile"

class ShowFeedView(InstaLoginRequiredMixin, DetailView):
    '''Display the feed for a Profile'''

    model = Profile
    template_name = "mini_insta/show_feed.html"
    context_object_name = "profile"

    def get_object(self):
        """Return the Profile associated with the authenticated User."""

        return self.get_logged_in_profile()

class SearchView(InstaLoginRequiredMixin, ListView):
    '''Search for Profiles and Posts'''

    template_name = 'mini_insta/search_results.html'
    context_object_name = 'posts'

    def dispatch(self, request, *args, **kwargs):
        '''Handle requests'''
        profile = self.get_logged_in_profile()
        if 'query' not in self.request.GET:
            return render(request,'mini_insta/search.html', {'profile': profile})

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        '''Return Posts matching the query'''
        query = self.request.GET.get('query')
        posts = Post.objects.filter(caption__contains=query)
        return posts

    def get_context_data(self, **kwargs):
        '''Add context variables'''
        context = super().get_context_data(**kwargs)
        profile = self.get_logged_in_profile()
        query = self.request.GET.get('query')
        # 
        profiles = Profile.objects.filter(username__contains=query) | Profile.objects.filter(display_name__contains=query) | Profile.objects.filter(bio_text__contains=query)

        context['profile'] = profile
        context['query'] = query
        context['profiles'] = profiles

        return context
    
class LogoutConfirmationView(TemplateView):
    '''Display a confirmation page after a user logs out'''

    template_name="mini_insta/logged_out.html"

class CreateProfileView(CreateView):
    '''Displays and process the form used to create a profile'''

    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"

    def get_context_data(self, **kwargs):
        '''Adding the UserCreationForm to the template context'''
        context = super().get_context_data(**kwargs)
        context["user_form"] = UserCreationForm()

        return context
    
    def form_valid(self, form):
        """Create a User and Profile from the submitted forms."""

        # Reconstructing the UserCreationForm from the data in the POST
        user_form = UserCreationForm(self.request.POST)

        # Making sure the user form is valid
        if not user_form.is_valid():
            return self.form_invalid(form)
        user = user_form.save()
        login(
            self.request,
            user,
            backend='django.contrib.auth.backends.ModelBackend'
        )

        form.instance.user = user
        return super().form_valid(form)
    
    def get_success_url(self):
        """Return the URL after successfully creating a Profile."""

        return reverse(
            'show_profile',
            kwargs={'pk': self.object.pk}
        )
    
class CreateFollowView(InstaLoginRequiredMixin, TemplateView):
    """Create a Follow relationship between two Profiles."""

    def dispatch(self, request, *args, **kwargs):
        """Create a Follow object and redirect to the Profile page."""

        current_profile = self.get_logged_in_profile()
        target_profile = Profile.objects.get(
            pk=self.kwargs["pk"]
        )

        # Prevent a Profile from following itself.
        if current_profile != target_profile:
            Follow.objects.get_or_create(follower_profile=current_profile, profile=target_profile)

        return redirect("show_profile", pk=target_profile.pk)
    
class DeleteFollowView(InstaLoginRequiredMixin, TemplateView):
    """Remove a Follow relationship between two Profiles."""

    def dispatch(self, request, *args, **kwargs):
        """Delete the Follow object and redirect to the Profile page."""

        current_profile = self.get_logged_in_profile()
        target_profile = Profile.objects.get(pk=self.kwargs["pk"])

        # Deleting any matching follow relationship
        Follow.objects.filter(follower_profile=current_profile, profile=target_profile).delete()

        return redirect("show_profile", pk=target_profile.pk)
    
class CreateLikeView(InstaLoginRequiredMixin, TemplateView):
    """Create a Like on a Post."""

    def dispatch(self, request, *args, **kwargs):
        """Create a Like object and redirect to the Post page."""

        current_profile = self.get_logged_in_profile()
        post = Post.objects.get(pk=self.kwargs["pk"])

        # Preventing the user form liking own post
        if current_profile != post.profile:
            Like.objects.get_or_create(profile=current_profile, post=post)

        return redirect("show_post", pk=post.pk)
    
class DeleteLikeView(InstaLoginRequiredMixin, TemplateView):
    """Remove a Like from a Post."""

    def dispatch(self, request, *args, **kwargs):
        """Delete a Like object and redirect to the Post page."""

        current_profile = self.get_logged_in_profile()
        post = Post.objects.get(pk=self.kwargs["pk"])
        Like.objects.filter(profile=current_profile, post=post).delete()

        return redirect("show_post", pk=post.pk)