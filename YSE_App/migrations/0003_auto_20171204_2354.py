# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_provider',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_country_code',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_first_three',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_last_four',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_provider_str',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
