from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''String representation of this model'''
        return f"User: {self.username}"