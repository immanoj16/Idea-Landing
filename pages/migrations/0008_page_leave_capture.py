# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20170321_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='leave_capture',
            field=models.BooleanField(default=True),
        ),
    ]
