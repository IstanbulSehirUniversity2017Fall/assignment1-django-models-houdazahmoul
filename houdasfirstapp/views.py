# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import PictureGallery
# we need to return http response step 5

# Create your views here.
def index(request):
    all_picture = PictureGallery.objects.all()
    html = ''
    for picture in all_picture:
        url = '/houdasfirstapp/' + str(picture.id) + '/'
        picture_caption = picture.caption
        picture_url = picture.picture
        picture_time = picture.share_date
        html += '<a href= "' + url + '">' + picture_caption + '</a> <br> <img src="' + picture_url + '">'


    return HttpResponse("<h1> Welcome to my first app which supposedly imitates a gallery -HOUDA </h1> <br>" + html)

def detail(request, picture_id):
    return HttpResponse("<h2>Details for album id:" + str(picture_id) + "</h2>")