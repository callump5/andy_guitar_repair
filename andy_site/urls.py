from django.conf.urls import url

from .views import get_landing, get_services, get_service

urlpatterns = [
    url(r'^$', get_landing, name='home'),

    url(r'services/$',get_services, name='services'),
    url(r'services/(?P<service_id>\d+)/$' , get_service, name='service')
]