# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20171001_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AddField(
            model_name='driver',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
