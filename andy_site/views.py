# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Service, Testimonials, JobBlogPost
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

    return render(request, 'home/home_page.html', args)


def get_services(request):

    services = Service.objects.all()
    job_posts = JobBlogPost.objects.all()

    testimonials = Testimonials.objects.all()

    if request.method == 'POST':
        contact_form = ContactRequestForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('services')
        else:
            contact_form = ContactRequestForm()
    else:
        contact_form = ContactRequestForm

    args = {
        'services': services,
        'job_posts': job_posts,
        'testimonials': testimonials,
        'form': contact_form
    }

    return render(request, 'services/services-page.html', args)


def get_service(request, service_id):

    service = Service.objects.get(pk=service_id)
    jobs = JobBlogPost.objects.filter(service_id=service_id)

    args = {
        'service': service,
        'jobs': jobs
    }

    return render(request, 'services/service-page.html', args)
