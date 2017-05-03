from django.conf.urls import url
from i0.views import *

urlpatterns = [
    url(r'^$', index0f, name='index0f'),
    # sites
	url(r'^f7/$', f7, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/$', bg, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<tp>(rgb|img|piet))/$', f7, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/(?P<tp>(rgb|img|piet))/$', bg, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<tp>rgb)/(?P<a>[01x])/(?P<b>[0])/(?P<c>([01x]|[01x]{3}|pb|rgb|piet|cmyx))/(?P<d>x)/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>rgb)/(?P<a>[01x])/(?P<b>[0])/(?P<c>([01x]|[01x]{3}|pb|rgb|piet|cmyx))/(?P<d>x)/(?P<e>[01x])/$', bg, name='bg'),
    url(r'^f7/(?P<tp>img)/(?P<a>[0])/(?P<b>[0])/\[(?P<c>.+\.(gif|jpg|jpeg|bmp))\]/(?P<d>x)/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>img)/(?P<a>[0])/(?P<b>[0])/\[(?P<c>.+\.(gif|jpg|jpeg|bmp))\]/(?P<d>x)/(?P<e>[01x])/$', bg, name='bg'),
    url(r'^f7/(?P<tp>piet)/(?P<a>[01x])/(?P<b>[01x]([01x]{0,3}|pb))/(?P<c>([01x]|[01x]{3}|pb|rgb|piet|cmyx))/(?P<d>x)/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>piet)/(?P<a>[01x])/(?P<b>[01x]([01x]{0,3}|pb))/(?P<c>([01x]|[01x]{3}|pb|rgb|piet|cmyx))/(?P<d>x)/(?P<e>[01x])/$', bg, name='bg'),
]
