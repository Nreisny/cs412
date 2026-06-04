# File: models.py
# Author: Nicholas Reis (nreisny@bu.edu) 5/30/26
# Description: Defines the models used by the Mini Insta application.

from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Represents a Mini Insta user profile'''
    username = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''String representation of this model'''
        return f"User: {self.username}"
    
    def get_all_posts(self):
        '''Returns all posts that are connected to this Profile'''
        posts = Post.objects.filter(profile=self)
        return posts
    
    def get_absolute_url(self):
        '''Return the URL to display one instance of this model.'''    
        return reverse('show_profile', kwargs={"pk": self.pk})
    
    def get_followers(self):
        '''returns a Querylist of followers of the given profile'''
        follower_list = []
        followers = Follow.objects.filter(profile=self)
        for follower in followers:
            follower_list.append(follower.follower_profile)
        return follower_list
    
    def get_num_followers(self):
        '''Returns the number of followers of the given profile'''
        follower_list = []
        followers = Follow.objects.filter(profile=self)
        for follower in followers:
            follower_list.append(follower.follower_profile)
        return len(follower_list)
    
    def get_following(self):
        '''Returns a QueryList of profiles that is being followed'''
        following_list = []
        following = Follow.objects.filter(follower_profile=self)
        for follow in following:
            following_list.append(follow.profile)
        return following_list
    
    def get_num_following(self):
        '''Retruns the number of profiles that is being followed'''
        following_list = []
        following = Follow.objects.filter(follower_profile=self)
        for follow in following:
            following_list.append(follow.profile)
        return len(following_list)
    
    def get_post_feed(self):
        '''Return all posts from profiles that this profile follows'''
        following = Follow.objects.filter(follower_profile=self)
        followed_profiles = []
        for follow in following:
            followed_profiles.append(follow.profile)
        posts = Post.objects.filter(profile__in=followed_profiles).order_by('-timestamp')
        return posts
        
class Post(models.Model):
    '''Represents a Mini Insta user Post'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''String representation of this Post model'''
        return f"Profile: {self.profile}, Caption: {self.caption}"
    
    def get_all_photos(self):
        '''Returns all Photo's that are connected to this Post'''
        photos = Photo.objects.filter(post=self)
        return photos

    def get_first_photo(self):
        '''Returns the first photo that is connected to this Post'''
        photos = Photo.objects.filter(post=self).first()
        return photos
    
    def get_absolute_url(self):
         '''Return the URL to display one instance of this model.''' 
         return reverse('show_post', kwargs={'pk': self.pk})
    
    def get_all_comments(self):
        return Comment.objects.filter(post=self)
    
    def get_likes(self):
        '''Return all likes for this Post'''
        return Like.objects.filter(post=self)

class Photo(models.Model):
    '''Represents a Mini Insta user Photo'''
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''String representation of this Photo Model'''
        if self.image_url:
            return self.image_url

        elif self.image_file:
            return str(self.image_file)

        return "No image"
    
    def get_image_url(self):
        '''Returns the URL for this iamge'''
        if self.image_url:
            return self.image_url
        elif self.image_file:
            return self.image_file.url
        
        return ""
    
class Follow(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile")
    follower_profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.username} follows {self.follower_profile.username}"

class Comment(models.Model):
    '''Represents a comment on a Post'''

    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        '''String representation of this Comment'''
        return f"{self.profile.username}: {self.text}"
    
    def get_all_comments(self):
        '''Return all comments for this Post'''
        return Comment.objects.filter(post=self)
    
class Like(models.Model):
    '''Represents a like on a Post'''

    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.username} likes Post {self.post.pk}"