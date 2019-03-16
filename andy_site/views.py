# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Service, Testimonials
from .forms import ContactRequestForm

# Create your views here.


def get_landing(request):
    services = Service.objects.all()
    testimonials = Testimonials.objects.all()

    args = {
        'services': services,
        'testimonials': testimonials
    }

    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base/base.html')

    return render(request, 'base/base.html', args)