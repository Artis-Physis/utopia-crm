# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-12 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0008_auto_20210315_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='extras',
            field=models.IntegerField(blank=True, null=True, verbose_name='Extras'),
        ),
    ]