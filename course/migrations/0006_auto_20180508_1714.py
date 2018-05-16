# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-08 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20180508_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='课程名称')),
                ('price', models.IntegerField(verbose_name='课程价格')),
                ('learn_time', models.CharField(max_length=10, verbose_name='课程时长')),
                ('nums', models.IntegerField(default=0, verbose_name='购买人数')),
                ('image', models.ImageField(upload_to='course/%Y/%m', verbose_name='课程封面')),
                ('describe', models.ImageField(upload_to='', verbose_name='课程简介')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击人数')),
            ],
            options={
                'verbose_name_plural': '第三类课程',
                'verbose_name': '第三类课程',
            },
        ),
        migrations.AlterModelOptions(
            name='courseclassthird',
            options={'verbose_name': '学科', 'verbose_name_plural': '学科'},
        ),
        migrations.RemoveField(
            model_name='courseclassthird',
            name='click_num',
        ),
        migrations.RemoveField(
            model_name='courseclassthird',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='courseclassthird',
            name='image',
        ),
        migrations.RemoveField(
            model_name='courseclassthird',
            name='learn_time',
        ),
        migrations.RemoveField(
            model_name='courseclassthird',
            name='nums',
        ),
        migrations.RemoveField(
            model_name='courseclassthird',
            name='price',
        ),
        migrations.AlterField(
            model_name='courseclassthird',
            name='name',
            field=models.CharField(max_length=30, verbose_name='学科名称'),
        ),
        migrations.AddField(
            model_name='course',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.CourseClassThird', verbose_name='第三分类'),
        ),
    ]
