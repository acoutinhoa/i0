# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f7', '0004_auto_20170520_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a',
            name='rel',
        ),
        migrations.RemoveField(
            model_name='b',
            name='rel',
        ),
        migrations.RemoveField(
            model_name='d',
            name='rel',
        ),
        migrations.DeleteModel(
            name='E',
        ),
        migrations.RemoveField(
            model_name='l8p',
            name='rel',
        ),
        migrations.RemoveField(
            model_name='v4r',
            name='rel',
        ),
        migrations.DeleteModel(
            name='A',
        ),
        migrations.DeleteModel(
            name='B',
        ),
        migrations.DeleteModel(
            name='B9',
        ),
        migrations.DeleteModel(
            name='D',
        ),
        migrations.DeleteModel(
            name='F7',
        ),
        migrations.DeleteModel(
            name='L8p',
        ),
        migrations.DeleteModel(
            name='T2',
        ),
        migrations.DeleteModel(
            name='V4r',
        ),
    ]