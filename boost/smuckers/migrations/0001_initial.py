# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_order', models.CharField(max_length=400)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BolItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packages', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=400)),
                ('weight', models.IntegerField(default=0)),
                ('bol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smuckers.Bol')),
            ],
        ),
    ]
