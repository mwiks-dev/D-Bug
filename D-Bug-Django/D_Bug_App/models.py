from django.db import models
from pygments.lexers import get_all_lexers
from django.conf import settings
# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    class Meta:
        ordering = ('created',)

class Comments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    class Meta:
        ordering = ('created',)