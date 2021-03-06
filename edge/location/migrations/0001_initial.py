# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-18 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('prev_lng', models.FloatField()),
                ('prev_lat', models.FloatField()),
            ],
            options={
                'db_table': 'devices',
            },
        ),
    ]
