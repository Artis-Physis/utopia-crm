# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-23 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0006_auto_20210318_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledtask',
            name='issue',
        ),
        migrations.AddField(
            model_name='scheduledtask',
            name='ends',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='support.ScheduledTask'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='support.IssueStatus'),
        ),
    ]
