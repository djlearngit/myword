# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-29 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0017_auto_20160529_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='column',
            field=models.ManyToManyField(default='\u516d\u7ea7', to='learn.Column', verbose_name='\u5206\u7c7b'),
        ),
    ]