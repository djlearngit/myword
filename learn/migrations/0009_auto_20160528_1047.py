# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-28 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0008_auto_20160528_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='home_display',
        ),
        migrations.RemoveField(
            model_name='column',
            name='nav_display',
        ),
    ]
