from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

# class User(AbstractUser):
#     pass

class Profile(models.Model):
    name = models.CharField(max_length=15,null=False)
    bio = models.TextField(max_length=200,null=False)
    email = models.EmailField()
    profile_picture = models.CloudinaryField('profile_picture',blank=True)
    languages = models.TextField(null=False)

    def __str__(self):
        return self.name

