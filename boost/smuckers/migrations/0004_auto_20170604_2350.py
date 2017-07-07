# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-04 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smuckers', '0003_auto_20170513_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='bol',
            name='dock_number',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='bol',
            name='seal_number',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='agents_number',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='bill_of_lading',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='car_initial',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bol',
            name='car_number',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bol',
            name='cosigned_to',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='county_of',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bol',
            name='delivering_carrier',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='destination',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='from_address',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='bol',
            name='route',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='shippers_number',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='shipping_order',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bol',
            name='state_of',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]