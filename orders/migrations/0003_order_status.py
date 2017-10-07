# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170620_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('C', 'Cancelled'), ('S', 'Start'), ('A', 'Accepted'), ('R', 'Realization'), ('P', 'Provider'), ('E', 'Ended')], default='S', max_length=1),
        ),
    ]
