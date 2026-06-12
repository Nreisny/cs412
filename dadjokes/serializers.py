# File: serializer.py
# Author: Nicholas Reis (nreisny@bu.edu) 6/11/26
# Description: Acts as a helper to serialize different models
#              to either send out or create

from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    '''A serializer for the Joke Model'''

    class Meta:
        model = Joke
        fields = ["joke", "name"]

        def create(self, validated_data):
            '''Overrides the super class method that handles object creation'''
            print(f'JokeSerializer.create, validated_data={validated_data}')

            return Joke.objects.create(**validated_data)
        
class PictureSerializer(serializers.ModelSerializer):
    '''A searializer for the Picture Model'''

    class Meta:
        model = Picture
        fields = ["image_url", "name"]

        def create(self, validated_data):
            '''Overrides the super class method that handles object creation'''

            print(f'PictureSeriazlier.create, validated_data={validated_data}')

            return Picture.objects.create(**validated_data)