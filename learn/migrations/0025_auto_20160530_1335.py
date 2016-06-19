# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-30 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0024_remove_user_daka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, default='', verbose_name='\u5185\u5bb9')),
                ('user_add', models.ManyToManyField(to='learn.User', verbose_name='\u5f52\u5c5e\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u7b14\u8bb0',
                'verbose_name_plural': '\u7b14\u8bb0',
            },
        ),
        migrations.RemoveField(
            model_name='word',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='wordfor',
            field=models.ManyToManyField(to='learn.Word', verbose_name='\u5f52\u5c5e\u5355\u8bcd'),
        ),
    ]