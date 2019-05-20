# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Service, Testimonials, JobBlogPost, About, PricingItem, ContactInfo, ImageContent
from .forms import ContactRequestForm

# Create your views here.


def get_landing(request):
    contact_info = ContactInfo.objects.all().first()
    landing_content = ImageContent.objects.first()
    image_content = ImageContent.objects.all()[1]
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
        'contact_info': contact_info,
        'landing_content': landing_content,
        'image_content': image_content,
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
    contact_info = ContactInfo.objects.all().first()
    image_content = ImageContent.objects.all()[:1]

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

        'contact_info': contact_info,
        'image_content': image_content,
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

    contact_info = ContactInfo.objects.all().first()
    landing_content = ImageContent.objects.first()
    image_content = ImageContent.objects.all()[1]
    about = About.objects.all()
    services = Service.objects.all()
    itemprices = PricingItem.objects.all()
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
        'jobs': jobs,
        'contact_info': contact_info,
        'landing_content': landing_content,
        'image_content': image_content,
        'about': about,
        'services': services,
        'itemprices': itemprices,
        'testimonials': testimonials,
        'form': contact_form
    }

    return render(request, 'projects/gallery.html', args)


def get_project(request, job_id):

    job_post = JobBlogPost.objects.get(pk=job_id)


    contact_info = ContactInfo.objects.all().first()
    landing_content = ImageContent.objects.first()
    image_content = ImageContent.objects.all()[1]
    about = About.objects.all()
    services = Service.objects.all()
    itemprices = PricingItem.objects.all()
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
        'job_post': job_post,

        'contact_info': contact_info,
        'landing_content': landing_content,
        'image_content': image_content,
        'about': about,
        'services': services,
        'itemprices': itemprices,
        'testimonials': testimonials,
        'form': contact_form
    }

    return render(request, 'projects/project.html', args)

def get_ssl(request):

    return render(request, '.well-known/pki-validation/starfield.html')