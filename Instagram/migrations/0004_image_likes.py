# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0003_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
