from django.conf.urls import url
from f7.views import *

urlpatterns = [
	url(r'^f7/$', f7, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/$', bg, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<tp>(rgb|img|piet|l8p))/$', f7, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/(?P<tp>(rgb|img|piet|l8p))/$', bg, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<tp>rgb)/(?P<a>[01x])/(?P<b>[0])/(?P<c>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<d>[vhx]\d*)/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>rgb)/(?P<a>[01x])/(?P<b>[0])/(?P<c>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<d>[vhx]\d*)/(?P<e>[01x])/$', bg, name='bg'),
    url(r'^f7/(?P<tp>img)/(?P<a>[0])/(?P<b>[0])/\[(?P<c>.+\.(gif|jpg|jpeg|bmp))\]/(?P<d>[vhx]\d*)/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>img)/(?P<a>[0])/(?P<b>[0])/\[(?P<c>.+\.(gif|jpg|jpeg|bmp))\]/(?P<d>[vhx]\d*)/(?P<e>[01x])/$', bg, name='bg'),
    url(r'^f7/(?P<tp>(piet|l8p))/(?P<a>[01x])/(?P<b>[01x]([01x]{0,3}|pb|def))/(?P<c>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<d>[vhx]\d*)/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<tp>(piet|l8p))/(?P<a>[01x])/(?P<b>[01x]([01x]{0,3}|pb|def))/(?P<c>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<d>[vhx]\d*)/(?P<e>[01x])/$', bg, name='bg'),
]
