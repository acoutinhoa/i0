# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f7', '0013_f7_r1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f7',
            name='r1',
            field=models.ManyToManyField(blank=True, to='f7.F7'),
        ),
    ]
