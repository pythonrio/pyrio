# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_auto_20151205_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicao',
            name='sobre',
            field=models.TextField(default='sobre evento'),
            preserve_default=False,
        ),
    ]