from rest_framework import serializers
from .models import Post, Comments,LANGUAGE_CHOICES

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    body = serializers.CharField(required=True, allow_blank=False, max_length=500)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance