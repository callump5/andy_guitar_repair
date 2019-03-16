# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Service(models.Model):
    service = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/images/services')

    def __unicode__(self):
        return self.service

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = ' Services'