# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-18 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_issue_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='route',
        ),
        migrations.AlterField(
            model_name='issue',
            name='answer_1',
            field=models.CharField(blank=True, choices=[(b'I1', 'Collected'), (b'L1', 'Delivered again'), (b'L2', 'Not delivered'), (b'L3', "Can't be delivered that way"), (b'L4', 'Delivered late'), (b'L5', 'Problems to be delivered'), (b'L6', 'Delivered in a specific way')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='subcategory',
            field=models.CharField(blank=True, choices=[(b'L01', 'Did not arrive'), (b'L02', 'Arrived late'), (b'L03', 'Arrived wet'), (b'L04', 'Changed delivery place'), (b'L05', 'Not delivered'), (b'L06', 'Delivered to a wrong place'), (b'L07', 'Wrong label'), (b'L08', 'Wrong invoice delivered'), (b'L10', 'Paused route'), (b'L11', "Invoice wasn't delivered"), (b'L99', 'Uncategorized logistics issue'), (b'I01', "Product doesn't belong"), (b'I02', 'Price issue'), (b'I03', 'Payment type issue'), (b'I04', 'Subscription not being billed'), (b'I05', 'Payment type change'), (b'I06', 'Collection issue'), (b'I07', 'Collection issue (inactive subscription)'), (b'I08', 'Credit card expiration'), (b'I09', 'Debt issue'), (b'I99', 'Uncategorized invoicing issue'), (b'C01', 'Suggestions'), (b'C02', 'Complaints'), (b'C03', 'Corrections'), (b'C04', 'Requests'), (b'C05', 'Contact journalist'), (b'C06', 'Forward content'), (b'W01', 'Access (sign-in)'), (b'W02', 'Registry (sign-up)'), (b'W03', 'Website not available'), (b'W04', 'Settings issue'), (b'W05', 'Articles limit reached'), (b'W06', 'Not using service'), (b'S01', 'Promotion request'), (b'S02', 'Register new subscription'), (b'S03', 'End subscription'), (b'S04', 'Schedule subscription pause'), (b'S05', 'Schedule address change'), (b'S06', 'Vacation (Resorts)'), (b'S07', 'Newsletters'), (b'S08', 'Complaints on service'), (b'S09', 'Payment types'), (b'S10', 'Errors in data'), (b'S11', 'Special cases'), (b'S12', 'Schedule task'), (b'S12', 'Change in subscription'), (b'O01', 'Community Benefits'), (b'O02', 'Community Events'), (b'O03', 'Caf\xe9'), (b'O04', 'Media-lab'), (b'O05', 'Shop'), (b'O06', 'Community Suggestions'), (b'O07', 'Community Complaints'), (b'O08', 'Community Requests'), (b'O09', 'Polls/Surveys'), (b'N/A', 'No sub-category')], max_length=3, null=True),
        ),
    ]
