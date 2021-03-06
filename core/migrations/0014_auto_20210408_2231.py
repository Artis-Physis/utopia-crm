# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-08 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_subscriptionproduct_label_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[(b'S', 'Subscription'), (b'N', 'Newsletter'), (b'D', 'Discount'), (b'P', 'Percentage discount'), (b'O', 'Other')], db_index=True, default='O', max_length=1),
        ),
    ]
