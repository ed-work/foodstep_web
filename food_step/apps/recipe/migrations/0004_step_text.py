# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
