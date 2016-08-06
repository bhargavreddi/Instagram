from __future__ import unicode_literals

import os

from django.contrib.auth.models import User
from django.db import models

from django.core.files.storage import FileSystemStorage

# PRIVATE_DIR = os.path.join('pictures', 'web-private')
# fs = FileSystemStorage(location=PRIVATE_DIR)

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    description = models.CharField(max_length=225,default='Image')
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User)

class Likes(models.Model):
    image = models.ForeignKey(Image)
    user = models.ForeignKey(User)

class Comments(models.Model):
    image = models.ForeignKey(Image)
    comment = models.TextField(max_length=225)
    user = models.ForeignKey(User)

class Follow(models.Model):
    user = models.ForeignKey(User,related_name='user')
    follower = models.ForeignKey(User,related_name='follower')