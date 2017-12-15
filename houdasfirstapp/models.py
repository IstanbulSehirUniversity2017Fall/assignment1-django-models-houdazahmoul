# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PhotoType(models.Model):
    photo_type = models.CharField(max_length=10)

class PictureGallery(models.Model):
    caption = models.CharField(max_length= 30)
    favorites = models.IntegerField(default=0)
    share_date = models.DateTimeField('Upload Date')
    picture = models.CharField(max_length = 1000)
    type = models.ForeignKey(PhotoType, on_delete=models.CASCADE)
# Create your models here.
