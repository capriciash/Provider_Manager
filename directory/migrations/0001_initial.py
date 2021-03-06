# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=56)),
                ('last_name', models.CharField(max_length=56)),
                ('driver_id', models.CharField(max_length=12)),
                ('birth_date', models.DateField()),
                ('hire_date', models.DateField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('eligible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business_name', models.CharField(max_length=56)),
                ('contract', models.FileField(upload_to='provider_contracts')),
                ('contract_start_date', models.DateField()),
                ('contract_end_date', models.DateField()),
                ('address', models.CharField(max_length=56)),
                ('phone_number', models.IntegerField()),
                ('business_license', models.CharField(max_length=18)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider_Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=56)),
                ('last_name', models.CharField(max_length=56)),
                ('title', models.CharField(max_length=56)),
                ('phone_number', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Provider')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Provider'),
        ),
    ]
