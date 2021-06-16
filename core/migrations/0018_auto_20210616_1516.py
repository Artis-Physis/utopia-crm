# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-16 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_subscriptionproduct_has_envelope'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='updated_from',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Subscription'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='inactivity_reason',
            field=models.IntegerField(blank=True, choices=[(1, 'Normal end'), (2, 'Paused'), (3, 'Upgraded'), (9, 'Lost the route'), (10, "We don't reach this address"), (11, 'Bad addition to the database'), (12, 'Duplicated address'), (13, 'Debtor'), (15, 'Vacations'), (16, 'Debtor, automatic unsubscription'), (99, 'N/A')], null=True, verbose_name='Inactivity reason'),
        ),
        migrations.AlterField(
            model_name='subscriptionproduct',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logistics.Route', verbose_name='Route'),
        ),
    ]