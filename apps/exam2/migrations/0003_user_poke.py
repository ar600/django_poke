# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam2', '0002_auto_20170904_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='poke',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
