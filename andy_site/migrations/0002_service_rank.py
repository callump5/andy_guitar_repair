# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andy_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='rank',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]