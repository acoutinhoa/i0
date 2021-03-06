# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e4', '0002_auto_20170619_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='B0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d0', models.DateTimeField(auto_now=True)),
                ('n0', models.CharField(max_length=100, verbose_name='nome_grupo')),
                ('blocos', models.ManyToManyField(blank=True, related_name='_b0_blocos_+', to='e4.B0')),
            ],
        ),
        migrations.CreateModel(
            name='I1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d0', models.DateTimeField(auto_now=True)),
                ('creditos', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, height_field='h', null=True, upload_to='e4/i1', width_field='w')),
            ],
        ),
        migrations.CreateModel(
            name='M0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d0', models.DateTimeField(auto_now=True)),
                ('n0', models.CharField(max_length=30, verbose_name='nome')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='obss')),
            ],
        ),
        migrations.CreateModel(
            name='T1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d0', models.DateTimeField(auto_now=True)),
                ('tt', models.CharField(max_length=30, verbose_name='titulo')),
                ('cit', models.TextField(verbose_name='citacao(info/linha)')),
                ('txt', models.TextField(verbose_name='txt')),
                ('ref', models.TextField(verbose_name='referencia/linha')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e4.A1')),
            ],
        ),
        migrations.RenameModel(
            old_name='P3',
            new_name='P0',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='blocos',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='imagens',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='informacoes',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='logos',
        ),
        migrations.RemoveField(
            model_name='b1',
            name='textos',
        ),
        migrations.RemoveField(
            model_name='i3',
            name='filme',
        ),
        migrations.RemoveField(
            model_name='m4',
            name='formatos',
        ),
        migrations.RemoveField(
            model_name='t3',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='t3',
            name='filme',
        ),
        migrations.RemoveField(
            model_name='f1',
            name='dx',
        ),
        migrations.AddField(
            model_name='i0',
            name='imagem',
            field=models.ImageField(blank=True, height_field='h', null=True, upload_to='e4/i0', width_field='w'),
        ),
        migrations.AlterField(
            model_name='p0',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e4.M0'),
        ),
        migrations.DeleteModel(
            name='B1',
        ),
        migrations.DeleteModel(
            name='I3',
        ),
        migrations.DeleteModel(
            name='M4',
        ),
        migrations.DeleteModel(
            name='T3',
        ),
        migrations.AddField(
            model_name='t1',
            name='filme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e4.F1'),
        ),
        migrations.AddField(
            model_name='m0',
            name='formatos',
            field=models.ManyToManyField(blank=True, through='e4.P0', to='e4.F0'),
        ),
        migrations.AddField(
            model_name='i1',
            name='filme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e4.F1'),
        ),
        migrations.AddField(
            model_name='b0',
            name='imagens',
            field=models.ManyToManyField(blank=True, to='e4.I1'),
        ),
        migrations.AddField(
            model_name='b0',
            name='informacoes',
            field=models.ManyToManyField(blank=True, to='e4.T0'),
        ),
        migrations.AddField(
            model_name='b0',
            name='logos',
            field=models.ManyToManyField(blank=True, to='e4.I0'),
        ),
        migrations.AddField(
            model_name='b0',
            name='textos',
            field=models.ManyToManyField(blank=True, to='e4.T1'),
        ),
    ]
