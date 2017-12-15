# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PictureGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=30)),
                ('favorites', models.IntegerField(default=0)),
                ('share_date', models.DateTimeField(verbose_name='Upload Date')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houdasfirstapp.PhotoType')),
            ],
        ),
    ]
