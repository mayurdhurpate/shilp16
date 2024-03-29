# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quriosity', '0003_question_response_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 5, 16, 6, 22, 253322, tzinfo=utc), verbose_name='end time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 5, 16, 6, 40, 797180, tzinfo=utc), verbose_name='start time'),
            preserve_default=False,
        ),
    ]
