# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-16 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andy_site', '0003_auto_20190316_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact Request',
                'verbose_name_plural': 'Contact Request',
            },
        ),
    ]