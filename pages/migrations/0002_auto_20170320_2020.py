# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='layout',
            field=models.CharField(choices=[('standard', 'Standard'), ('stacked', 'Stacked')], default='standard', max_length=20),
        ),
        migrations.AddField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#000000', max_length=6),
        ),
        migrations.AddField(
            model_name='page',
            name='show_nav',
            field=models.BooleanField(default=True),
        ),
    ]
