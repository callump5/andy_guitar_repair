# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import About, Service, Testimonials, GalleryPost, ContactRequest, ContactInfo, PricingItem, ImageContent

from django.contrib import admin

admin.site.register(About)
admin.site.register(Service)
admin.site.register(PricingItem)
admin.site.register(Testimonials)
admin.site.register(GalleryPost)
admin.site.register(ContactRequest)
admin.site.register(ContactInfo)
admin.site.register(ImageContent)


# Register your models here.
