# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servermon', '0007_auto_20171126_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='ipaddress',
            field=models.CharField(max_length=30),
        ),
    ]