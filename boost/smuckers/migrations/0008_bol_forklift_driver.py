# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smuckers', '0007_forkliftdriver'),
    ]

    operations = [
        migrations.AddField(
            model_name='bol',
            name='forklift_driver',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='smuckers.ForkliftDriver'),
        ),
    ]
