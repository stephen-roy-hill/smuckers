# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smuckers', '0009_auto_20170724_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
