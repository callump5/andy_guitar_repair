# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-10 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('andy_site', '0012_pricingcate_pricingitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactrequest',
            old_name='client',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='pricingitem',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='andy_site.Service'),
        ),
        migrations.DeleteModel(
            name='PricingCate',
        ),
    ]
