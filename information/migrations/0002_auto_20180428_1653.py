# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-28 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='手机'),
        ),
    ]