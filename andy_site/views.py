# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Service, Testimonials, JobBlogPost, About, PricingItem
from .forms import ContactRequestForm

# Create your views here.


def get_landing(request):
    about = About.objects.all()
    services = Service.objects.all()
    itemprices = PricingItem.objects.all()
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
        'about': about,
        'services': services,
        'itemprices': itemprices,
        'testimonials': testimonials,
        'form': contact_form
    }

    return render(request, 'home/home_page.html', args)


def get_services(request):

    services = Service.objects.all()
    job_posts = JobBlogPost.objects.all()[:5]

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
        'service': service,
        'jobs': jobs,
        'form': contact_form
    }

    return render(request, 'services/service-page.html', args)


def get_galley(request):

    jobs = JobBlogPost.objects.all()

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
        'jobs': jobs,
        'form': contact_form
    }

    return render(request, 'projects/gallery.html', args)


def get_project(request, job_id):

    job_post = JobBlogPost.objects.get(pk=job_id)

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
        'job_post': job_post,
        'form': contact_form
    }

    return render(request, 'projects/project.html', args)