# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='B9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='E',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='F7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='L8p',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
                ('f7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f7.F7')),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='T2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='V4r',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('info', models.TextField()),
                ('d0', models.DateTimeField(auto_now_add=True)),
                ('t2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f7.T2')),
            ],
            options={
                'ordering': ['?'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='d',
            name='f7',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f7.F7'),
        ),
        migrations.AddField(
            model_name='b',
            name='t2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f7.T2'),
        ),
        migrations.AddField(
            model_name='a',
            name='b9',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f7.B9'),
        ),
    ]