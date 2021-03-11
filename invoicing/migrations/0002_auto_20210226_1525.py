# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-26 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='payment_type',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_type',
            field=models.CharField(max_length=2, verbose_name='Payment type'),
        ),
    ]