# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0022_user_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='daka',
            field=models.IntegerField(default=0),
        ),
    ]
