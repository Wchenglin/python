# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-24 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20181023_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default=uuid.uuid1, max_length=100, primary_key=True, serialize=False),
        ),
    ]
