from django.conf.urls import url

from .views import get_landing, get_services

urlpatterns = [
    url(r'^$', get_landing, name='home'),
    url(r'services/$',get_services, name='services')
]