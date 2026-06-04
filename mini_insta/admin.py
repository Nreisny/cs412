# File: admin.py
# Author: Nicholas Reis (nreisny@bu.edu) 5/28/26
# Description: Registering our models to the admin

from django.contrib import admin
from .models import Profile, Post, Photo, Follow, Comment, Like
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)