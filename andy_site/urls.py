from django.conf.urls import url

from .views import get_landing, get_services, get_service, get_galley, get_robots, get_ssl, get_sitemap, get_htaccess

urlpatterns = [
    url(r'^$', get_landing, name='home'),

    url(r'services/$',get_services, name='services'),
    url(r'services/(?P<service_slug>[\w-]+)/$' , get_service, name='service'),

    url(r'project-gallery/$', get_galley, name='gallery'),

    url(r'.well-known/pki-validation/starfield.html', get_ssl),
    url(r'sitemap.xml', get_sitemap),
    url(r'robots.txt', get_robots),
    url(r'.htaccess', get_htaccess)
]