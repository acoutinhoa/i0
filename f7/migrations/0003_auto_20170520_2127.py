# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f7', '0002_auto_20170520_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a',
            name='b9',
        ),
        migrations.RemoveField(
            model_name='b',
            name='t2',
        ),
        migrations.RemoveField(
            model_name='d',
            name='f7',
        ),
        migrations.RemoveField(
            model_name='l8p',
            name='f7',
        ),
        migrations.RemoveField(
            model_name='v4r',
            name='t2',
        ),
        migrations.AddField(
            model_name='a',
            name='r3',
            field=models.ManyToManyField(to='f7.B9'),
        ),
        migrations.AddField(
            model_name='b',
            name='r3',
            field=models.ManyToManyField(to='f7.T2'),
        ),
        migrations.AddField(
            model_name='d',
            name='r3',
            field=models.ManyToManyField(to='f7.F7'),
        ),
        migrations.AddField(
            model_name='l8p',
            name='r3',
            field=models.ManyToManyField(to='f7.F7'),
        ),
        migrations.AddField(
            model_name='v4r',
            name='r3',
            field=models.ManyToManyField(to='f7.T2'),
        ),
    ]