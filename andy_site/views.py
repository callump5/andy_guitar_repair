# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Service, Testimonials
from .forms import ContactRequestForm

# Create your views here.


def get_landing(request):
    services = Service.objects.all()
    testimonials = Testimonials.objects.all()

    if request.method == 'POST':
        contact_form = ContactRequestForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('home')
        else:
             contact_form = ContactRequestForm()
    else:
        contact_form = ContactRequestForm
    args = {
        'services': services,
        'testimonials': testimonials,
        'form': contact_form
    }

    return render(request, 'base/base.html', args)