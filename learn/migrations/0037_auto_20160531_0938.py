# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-31 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0036_auto_20160531_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='\u4f5c\u8005')),
                ('content', models.TextField(blank=True, default='', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u5355\u8bcd',
                'verbose_name_plural': '\u5355\u8bcd',
            },
        ),
        migrations.RemoveField(
            model_name='word',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='word',
            field=models.ManyToManyField(to='learn.Word', verbose_name='\u5f52\u5c5e\u5355\u8bcd'),
        ),
    ]
