# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smuckers', '0006_bol_truck_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForkliftDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
