# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-24 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20181023_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='parking_id',
            field=models.CharField(default=uuid.uuid1, max_length=32, primary_key=True, serialize=False),
        ),
    ]