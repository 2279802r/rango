# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-26 20:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20170126_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 1, 26, 20, 8, 46, 902000, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
