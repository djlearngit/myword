# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-31 03:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0040_auto_20160531_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(default=datetime.date(2012, 12, 7), null=True, verbose_name='\u65f6\u95f4'),
        ),
    ]
