from rest_framework import serializers
from .models import Post, Comments,LANGUAGE_CHOICES

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created','language']
