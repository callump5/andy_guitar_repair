# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Service

# Create your views here.


def get_landing(request):
    services = Service.objects.all()
    args = {
        'services': services
    }
    return render(request, 'base/base.html', args)