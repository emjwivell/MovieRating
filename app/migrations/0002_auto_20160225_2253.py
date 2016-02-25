# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 22:53
from __future__ import unicode_literals

from django.db import migrations

from app.models import Review, Rater, Movie


def load_data_movie(*args):
   with open("/Users/emilywivell/PycharmProjects/MovieReviews/app/static/ml-100k/u.item", encoding="ISO-8859-1") as movies:
       for movie in movies.readlines():
           line = movie.split("|")
           Movie.objects.create(pk=line[0], movie_title=line[1],
                                release_date=line[2], video_release_date=line[3],
                                imdb=line[4], unknown_genre=line[5],
                                action=line[6], adventure=line[7],
                                animation=line[8], childrens=line[9],
                                comedy=line[10], crime=line[11],
                                documentary=line[12], drama=line[13],
                                fantasy=line[14], filmnoir=line[15],
                                horror=line[16], musical=line[17],
                                mystery=line[18], romance=line[19],
                                scifi=line[20], thriller=line[21],
                                war=line[22], western=line[23])


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(load_data_movie)

    ]

