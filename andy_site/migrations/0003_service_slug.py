# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-08 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andy_site', '0002_service_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
