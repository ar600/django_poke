# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam2', '0003_user_poke'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(null=True)),
                ('counter', models.IntegerField(default=0, null=True)),
                ('total', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='poke',
        ),
        migrations.RemoveField(
            model_name='user',
            name='poke_by',
        ),
        migrations.AddField(
            model_name='poke',
            name='poked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokedpokes', to='exam2.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokerpokes', to='exam2.User'),
        ),
    ]
