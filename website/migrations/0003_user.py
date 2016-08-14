# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-13 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_pptuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('teamname', models.CharField(max_length=100)),
                ('teamleader', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('mob_no', models.CharField(max_length=15)),
                ('year', models.CharField(max_length=15)),
                ('college', models.CharField(max_length=15)),
                ('tmem1', models.CharField(blank=True, max_length=100)),
                ('email1', models.CharField(blank=True, max_length=100)),
                ('mob1', models.CharField(blank=True, max_length=15)),
                ('tmem2', models.CharField(blank=True, max_length=100)),
                ('email2', models.CharField(blank=True, max_length=100)),
                ('mob2', models.CharField(blank=True, max_length=100)),
                ('tmem3', models.CharField(blank=True, max_length=100)),
                ('email3', models.CharField(blank=True, max_length=100)),
                ('mob3', models.CharField(blank=True, max_length=100)),
                ('tmem4', models.CharField(blank=True, max_length=100)),
                ('email4', models.CharField(blank=True, max_length=100)),
                ('mob4', models.CharField(blank=True, max_length=100)),
                ('tmem5', models.CharField(blank=True, max_length=100)),
                ('email5', models.CharField(blank=True, max_length=100)),
                ('mob5', models.CharField(blank=True, max_length=100)),
                ('query', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]