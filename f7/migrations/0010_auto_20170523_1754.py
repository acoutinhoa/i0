# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f7', '0009_auto_20170523_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f7',
            name='n3',
            field=models.CharField(max_length=30),
        ),
    ]
