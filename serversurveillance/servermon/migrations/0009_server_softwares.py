# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servermon', '0008_auto_20171127_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='softwares',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
