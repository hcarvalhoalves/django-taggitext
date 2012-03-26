from django.conf.urls.defaults import *

urlpatterns = patterns('taggitext.views',
    url(r'^search/$', 'search_tags', name='taggitext-search'),
)
