# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m8', '0003_c0_m8'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m8',
            name='peso',
            field=models.FloatField(),
        ),
    ]
