# File: admin.py
# Author: Nicholas Reis (nreisny@bu.edu) 5/28/26
# Description: Registering our models to the admin

from django.contrib import admin
from .models import Profile, Post, Photo
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)