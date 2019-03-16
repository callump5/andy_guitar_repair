# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Service, Testimonials

# Create your views here.


def get_landing(request):
    services = Service.objects.all()
    testimonials = Testimonials.objects.all()

    args = {
        'services': services,
        'testimonials': testimonials
    }

    return render(request, 'base/base.html', args)