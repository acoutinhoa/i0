# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e4', '0009_auto_20170620_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='i0',
            old_name='imagem',
            new_name='img',
        ),
        migrations.AddField(
            model_name='i0',
            name='h',
            field=models.CharField(default='', editable=False, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='i0',
            name='w',
            field=models.CharField(default='', editable=False, max_length=10),
            preserve_default=False,
        ),
    ]