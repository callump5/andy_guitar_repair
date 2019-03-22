# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Service(models.Model):
    service = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/images/services')
    price =  models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.service

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class JobBlogPost(models.Model):
    title = models.CharField(max_length=300)
    service = models.ForeignKey(Service, related_name='job_post_service')
    description = models.TextField()
    image1 = models.ImageField(upload_to='uploads/images/jobposts')
    image2 = models.ImageField(upload_to='uploads/images/jobposts', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/images/jobposts', blank=True, null=True)


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

    client = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()

    def __unicode__(self):
        return self.client

    class Meta:
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Request'

