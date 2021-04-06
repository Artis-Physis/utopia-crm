# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-09 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0004_auto_20210211_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='route',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='State'),
        ),
    ]