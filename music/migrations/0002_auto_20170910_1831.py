# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='game_category',
            new_name='music_category',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='reloease_date',
            new_name='release_date',
        ),
    ]
