# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160227_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ureview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_review', models.TextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
