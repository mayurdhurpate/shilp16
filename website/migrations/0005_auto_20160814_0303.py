# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-13 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reguser',
            old_name='radio',
            new_name='college',
        ),
        migrations.AddField(
            model_name='reguser',
            name='event',
            field=models.CharField(default='q', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='teamname',
            field=models.CharField(default='e', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguser',
            name='year',
            field=models.CharField(default='1', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reguser',
            name='email1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='email2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='email3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='email4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='email5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='mob1',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='mob2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='mob3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='mob4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='mob5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='query',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='tmem1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='tmem2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='tmem3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='tmem4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='reguser',
            name='tmem5',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]