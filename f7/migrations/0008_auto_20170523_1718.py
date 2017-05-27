# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('f7', '0007_auto_20170523_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f7',
            name='r1',
        ),
        migrations.AddField(
            model_name='f7',
            name='r1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='f7.F7'),
        ),
        migrations.RemoveField(
            model_name='f7',
            name='t2',
        ),
        migrations.AddField(
            model_name='f7',
            name='t2',
            field=models.ManyToManyField(to='f7.T2'),
        ),
    ]
