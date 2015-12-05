# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 18:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20151205_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programa',
            name='data',
        ),
        migrations.AddField(
            model_name='programa',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2015, 12, 5, 18, 54, 21, 905777, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
