# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smuckers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bol',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
