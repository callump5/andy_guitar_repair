# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Service, Testimonials, JobBlogPost, ContactRequest

from django.contrib import admin

admin.site.register(Service)
admin.site.register(Testimonials)
admin.site.register(JobBlogPost)
admin.site.register(ContactRequest)


# Register your models here.
