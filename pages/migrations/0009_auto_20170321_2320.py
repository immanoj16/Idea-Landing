# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_page_leave_capture'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='jumbotron_bgcolor',
            field=models.CharField(default='#eeeeee', max_length=7, validators=[pages.models.layout_validator]),
        ),
        migrations.AddField(
            model_name='page',
            name='jumbotron_text_color',
            field=models.CharField(default='#000000', max_length=7, validators=[pages.models.layout_validator]),
        ),
        migrations.AlterField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#000000', max_length=7, validators=[pages.models.layout_validator]),
        ),
    ]
