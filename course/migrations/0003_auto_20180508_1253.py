# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-08 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_buy_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseclassthird',
            name='learn_time',
            field=models.IntegerField(max_length=10, verbose_name='课程时长'),
        ),
    ]
