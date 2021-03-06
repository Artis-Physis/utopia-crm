# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-19 19:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210318_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactproducthistory',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_contacts', to='core.Address', verbose_name='Billing address'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Campaign', verbose_name='Campaign'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='unsubscription_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Unsubscription manager'),
        ),
        migrations.AlterField(
            model_name='subscriptionproduct',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Address'),
        ),
        migrations.AlterField(
            model_name='subscriptionproduct',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='route', to='logistics.Route', verbose_name='Route'),
        ),
    ]
