# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quriosity', '0002_helpquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('score', models.IntegerField(verbose_name='score')),
                ('answer', models.CharField(max_length=40, verbose_name='answer')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=40, verbose_name='response')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quriosity.Question')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quriosity.Team')),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='slot')),
                ('question', models.ManyToManyField(to='quriosity.Question')),
            ],
            options={
                'verbose_name': 'Slot',
                'verbose_name_plural': 'Slots',
            },
        ),
    ]
