# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0005_auto_20171008_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='contract_end_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='contract_start_date',
            new_name='start_date',
        ),
    ]
