# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0028_auto_20160530_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_add',
            field=models.ManyToManyField(to='learn.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='wordfor',
            field=models.ManyToManyField(to='learn.Word'),
        ),
    ]
