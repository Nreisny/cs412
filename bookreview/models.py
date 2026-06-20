from django.db import models

class Profile(models.Model):
    '''th'''
    username = models.CharField(max_length=30)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User: {self.username}"
    
    def get_all_book_comments(self):
        return BookCommment.objects.filter(profile=self)
    
    def get_all_character_comments(self):
        return CharacterComment.objects.filter(profile=self)

class Book(models.Model):
    name = models.CharField(max_length=200)
    book_image_url = models.URLField(blank=True)
    synopsis = models.TextField(blank=True)
    author = models.CharField(max_length=60)
    rating = models.IntegerField(blank=True)

    def __str__(self):
        return f"Book Name: {self.name}"
    
    def get_all_comments(self):
        return BookCommment.objects.filter(book=self)
    
    def get_all_characters(self):
        return Character.objects.filter(book=self)
    
class Character(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    character_image_url = models.URLField(blank=True)
    rating = models.IntegerField(blank=True)

    def __str__(self):
        return f"Character Name: {self.name}"
    
    def get_all_comments(self):
        return Character.objects.filter(character=self)
    
class BookCommment(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.profile.username}: {self.text}"
    
class CharacterComment(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    text = models.TextField(blank=True)

