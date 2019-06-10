from django_hosts import patterns, host

host_patterns = patterns('path.to',
    host(r'www', 'andy_site.urls', name='www'),
)