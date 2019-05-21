# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Service, Testimonials, GalleryPost, About, PricingItem, ContactInfo, ImageContent
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
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
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
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            return redirect('services')
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

    return render(request, 'services/services-page.html', args)


def get_service(request, service_id):

    service = Service.objects.get(pk=service_id)
    jobs = GalleryPost.objects.filter(service_id=service_id)

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
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            return redirect('services')
        else:
            contact_form = ContactRequestForm()
    else:
        contact_form = ContactRequestForm

    args = {
        'service': service,
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

    return render(request, 'services/service-page.html', args)


def get_galley(request):

    jobs = GalleryPost.objects.all()

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
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
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

    job_post = GalleryPost.objects.get(pk=job_id)


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
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
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