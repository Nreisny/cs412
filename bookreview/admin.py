from django.contrib import admin
from .models import Profile, Book, Character, BookCommment, CharacterComment
# Register your models here.

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Character)
admin.site.register(BookCommment)
admin.site.register(CharacterComment)