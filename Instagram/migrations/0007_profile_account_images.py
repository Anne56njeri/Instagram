# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0006_auto_20180511_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_images',
            field=models.ManyToManyField(related_name='image', to='Instagram.Image'),
        ),
    ]
