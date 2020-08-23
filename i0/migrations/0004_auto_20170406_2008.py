# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('i0', '0003_auto_20170406_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='TXT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tt', models.CharField(blank=True, max_length=400)),
                ('dt', models.DateField(blank=True)),
                ('hr', models.TimeField(blank=True)),
                ('txt', models.TextField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='i0',
            name='cn',
            field=models.SlugField(blank=True, default='', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='txt',
            name='i0',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='i0.I0'),
        ),
        migrations.AddField(
            model_name='txt',
            name='tp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='i0.TP'),
        ),
    ]
