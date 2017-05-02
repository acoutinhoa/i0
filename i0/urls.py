from django.conf.urls import url
from i0.views import *

urlpatterns = [
    url(r'^$', index0f, name='index0f'),
    # sites
    url(r'^f7/$', f7, {'tp':'', 'a':'', 'b':'', 'c':'',}, name='f7'),
    url(r'^bg/$', bg, {'tp':'', 'a':'', 'b':'', 'c':'',}, name='bg'),
    url(r'^f7/(?P<tp>rgb)/(?P<a>[0-2])/(?P<b>[0-1])/(?P<c>([01x]{3}|pb|rgb|piet))/$', f7, name='f7'),
    url(r'^bg/(?P<tp>rgb)/(?P<a>[0-2])/(?P<b>[0-1])/(?P<c>([01x]{3}|pb|rgb|piet))/$', bg, name='bg'),
    url(r'^f7/(?P<tp>img)/(?P<a>[0])/(?P<b>[0-1])/(?P<c>.+\.(gif|jpg|jpeg|bmp))/$', f7, name='f7'),
    url(r'^bg/(?P<tp>img)/(?P<a>[0])/(?P<b>[0-1])/(?P<c>.+\.(gif|jpg|jpeg|bmp))/$', bg, name='bg'),
]
