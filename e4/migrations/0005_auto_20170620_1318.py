# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e4', '0004_f1_t0'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f1',
            name='ano',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='f1',
            name='diretores',
            field=models.ManyToManyField(blank=True, to='e4.D1'),
        ),
        migrations.AlterField(
            model_name='f1',
            name='sinopse',
            field=models.TextField(blank=True, null=True),
        ),
    ]