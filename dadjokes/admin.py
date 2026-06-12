# File: admin.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/11/26
# Description: Just telling our admin of the models we created

from django.contrib import admin
from .models import Picture, Joke

# Register your models here.
admin.site.register({Picture})
admin.site.register(Joke)