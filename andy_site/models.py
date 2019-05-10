# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
import os

# Create your models here.



def upload_site_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return '%s%s' % (
        filename_base,
        filename_ext.lower(),
    )



class About(models.Model):
    about = models.TextField()


    def __unicode__(self):
        return 'Info' + ' - ' + str(self.id)

    class Meta:
        verbose_name = 'About Text'
        verbose_name_plural = 'About Text'



class Service(models.Model):
    service = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_site_img)

    def __unicode__(self):
        return self.service

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'



class PricingItem(models.Model):
    cate = models.ForeignKey(Service)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return  str(self.cate.service) + ' - ' + self.name

    class Meta:
        verbose_name = 'Service Price'
        verbose_name_plural = 'Service Prices'



class JobBlogPost(models.Model):
    title = models.CharField(max_length=300)
    service = models.ForeignKey(Service, related_name='job_post_service')
    description = models.TextField()
    image1 = models.ImageField(upload_to=upload_site_img)
    image2 = models.ImageField(upload_to=upload_site_img, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_site_img, blank=True, null=True)


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Job Blog Post'
        verbose_name_plural = 'Job Blog Posts'




class Testimonials(models.Model):
    job = models.ForeignKey(JobBlogPost, related_name='job_post_testimonial')
    client = models.CharField(max_length=200)
    testimonial = models.TextField()

    def __unicode__(self):
        return self.client

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'



class ContactRequest(models.Model):

    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Request'

