from django.conf.urls import url

from .views import get_landing

urlpatterns = [
    url(r'^$', get_landing, name='home'),
]