# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-23 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20181023_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
