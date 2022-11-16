# Generated by Django 4.0.5 on 2022-11-16 08:23

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('D_Bug_Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('bio', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='profile_picture')),
                ('languages', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
