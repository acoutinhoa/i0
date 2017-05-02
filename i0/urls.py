from django.conf.urls import url
from i0.views import *

urlpatterns = [
    url(r'^$', index0f, name='index0f'),
    # sites
	url(r'^f7/$', f7, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/$', bg, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<tp>(rgb|img))/$', f7, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/(?P<tp>(rgb|img))/$', bg, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<tp>rgb)/(?P<a>[0-2])/(?P<b>[0])/(?P<c>([01x]{3}|pb|rgb|piet|cmyx))/(?P<d>x)/(?P<e>[0-2])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>rgb)/(?P<a>[0-2])/(?P<b>[0])/(?P<c>([01x]{3}|pb|rgb|piet|cmyx))/(?P<d>x)/(?P<e>[0-2])/$', bg, name='bg'),
    url(r'^f7/(?P<tp>img)/(?P<a>[0])/(?P<b>[0])/(?P<c>.+\.(gif|jpg|jpeg|bmp))/(?P<d>x)/(?P<e>[0-2])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>img)/(?P<a>[0])/(?P<b>[0])/(?P<c>.+\.(gif|jpg|jpeg|bmp))/(?P<d>x)/(?P<e>[0-2])/$', bg, name='bg'),
]
