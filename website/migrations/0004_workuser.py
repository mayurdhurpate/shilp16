# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-12 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]