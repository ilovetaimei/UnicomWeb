# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-16 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='community',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='net_groupid_id',
            field=models.IntegerField(null=True),
        ),
    ]
