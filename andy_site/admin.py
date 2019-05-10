# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import About, Service, Testimonials, JobBlogPost, ContactRequest, ContactInfo, PricingItem

from django.contrib import admin

admin.site.register(About)
admin.site.register(Service)
admin.site.register(PricingItem)
admin.site.register(Testimonials)
admin.site.register(JobBlogPost)
admin.site.register(ContactRequest)
admin.site.register(ContactInfo)


# Register your models here.
