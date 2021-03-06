# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('f7', '0005_auto_20170523_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='F7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n3', models.CharField(max_length=10)),
                ('d0', models.DateTimeField(auto_now_add=True)),
                ('r1', models.ManyToManyField(related_name='_f7_r1_+', to='f7.F7')),
            ],
            options={
                'ordering': ['?'],
            },
        ),
        migrations.CreateModel(
            name='V4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n3', models.CharField(max_length=10)),
                ('d0', models.DateTimeField(auto_now_add=True)),
                ('r1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='f7.V4')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='f7',
            name='v4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f7.V4'),
        ),
    ]
