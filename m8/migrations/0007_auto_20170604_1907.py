# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-04 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('m8', '0006_auto_20170531_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='F8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['?'],
            },
        ),
        migrations.CreateModel(
            name='T2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['?'],
            },
        ),
        migrations.AddField(
            model_name='m8',
            name='familia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='m8.F8'),
        ),
        migrations.AddField(
            model_name='m8',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='m8.T2'),
        ),
    ]
