# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-08-09 12:33
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0010_auto_20210519_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='the_geom',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=32721),
        ),
    ]
