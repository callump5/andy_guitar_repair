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


class ImageContent(models.Model):
    text = models.TextField()


    def __unicode__(self):
        return 'Text' + ' - ' + str(self.id)

    class Meta:
        verbose_name = 'Image Text'
        verbose_name_plural = 'Image Texts'



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



class GalleryPost(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image1 = models.ImageField(upload_to=upload_site_img)
    image2 = models.ImageField(upload_to=upload_site_img, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_site_img, blank=True, null=True)

    tag1 = models.CharField(max_length=200, blank=True, null=True)
    tag2 = models.CharField(max_length=200, blank=True, null=True)
    tag3 = models.CharField(max_length=200, blank=True, null=True)
    tag4 = models.CharField(max_length=200, blank=True, null=True)
    tag5 = models.CharField(max_length=200, blank=True, null=True)
    tag6 = models.CharField(max_length=200, blank=True, null=True)
    tag7 = models.CharField(max_length=200, blank=True, null=True)
    tag8 = models.CharField(max_length=200, blank=True, null=True)
    tag9 = models.CharField(max_length=200, blank=True, null=True)


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery Post'
        verbose_name_plural = 'Gallery Posts'




class Testimonials(models.Model):
    job = models.ForeignKey(GalleryPost, related_name='job_post_testimonial')
    client = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
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


class ContactInfo(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=400)
    facebook = models.CharField(max_length=500)
    youtube = models.CharField(max_length=500)


    def __unicode__(self):
        return 'My Contact Info'

    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Infos'
