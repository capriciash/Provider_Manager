# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0008_auto_20171018_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefensiveDriving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_date', models.DateField()),
                ('time_since', models.DurationField()),
                ('cert_file', models.FileField(upload_to='Training_Certificates')),
                ('granting_agency', models.CharField(max_length=255)),
                ('instructor', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('name', models.CharField(default='Defensive Driving', max_length=255)),
                ('expiration', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Driver')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FirstAidCPR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_date', models.DateField()),
                ('time_since', models.DurationField()),
                ('cert_file', models.FileField(upload_to='Training_Certificates')),
                ('granting_agency', models.CharField(max_length=255)),
                ('instructor', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('name', models.CharField(default='First Aid and CPR', max_length=255)),
                ('expiration', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Driver')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]