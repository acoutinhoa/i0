from django.conf.urls import url
from f7.views import *

urlpatterns = [
	url(r'^f7/$', f7, {'f7tp':'', 'l8p':'', 'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/$', bg, {'f7tp':'', 'l8p':'', 'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<f7tp>[012])(?P<l8p>[-01x]?)/$', f7, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/(?P<f7tp>[012])(?P<l8p>[-01x]?)/$', bg, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<f7tp>[01])(?P<l8p>[-01x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/$', f7, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/(?P<f7tp>[01])(?P<l8p>[-01x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/$', bg, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<f7tp>[01])(?P<l8p>[-01x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<a>[01x])/(?P<b>[01x])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<f7tp>[01])(?P<l8p>[-01x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<a>[01x])/(?P<b>[01x])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', bg, name='bg'),
    url(r'^f7/(?P<f7tp>2)(?P<l8p>[-01x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/$', f7, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^bg/(?P<f7tp>2)(?P<l8p>[-01x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/$', bg, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='bg'),
    url(r'^f7/(?P<f7tp>2)(?P<l8p>[-01x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/(?P<a>[0])/(?P<b>[0])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^bg/(?P<f7tp>2)(?P<l8p>[-01x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/(?P<a>[0])/(?P<b>[0])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', bg, name='bg'),
]
