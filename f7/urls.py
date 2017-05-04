from django.conf.urls import url
from f7.views import *

urlpatterns = [
	url(r'^f7/$', f7, {'f7tp':'', 'l8p':'', 'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^b9/$', b9, {'f7tp':'', 'l8p':'', 'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='b9'),
    url(r'^f7/(?P<f7tp>(pi3t|rg6|im9))(?P<l8p>[012x]?)/$', f7, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^b9/(?P<f7tp>(pi3t|rg6|im9))(?P<l8p>[012x]?)/$', b9, {'tp':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='b9'),
    url(r'^f7/(?P<f7tp>(pi3t|rg6))(?P<l8p>[012x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/$', f7, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^b9/(?P<f7tp>(pi3t|rg6))(?P<l8p>[012x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/$', b9, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='b9'),
    url(r'^f7/(?P<f7tp>(pi3t|rg6))(?P<l8p>[012x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<a>[01x])/(?P<b>[01x])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^b9/(?P<f7tp>(pi3t|rg6))(?P<l8p>[012x]?)/(?P<tp>([01x]{3}|x|pb|rgb|piet|cmyx|def))/(?P<a>[01x])/(?P<b>[01x])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', b9, name='b9'),
    url(r'^f7/(?P<f7tp>im9)(?P<l8p>[012x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/$', f7, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^b9/(?P<f7tp>im9)(?P<l8p>[012x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/$', b9, {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='b9'),
    url(r'^f7/(?P<f7tp>im9)(?P<l8p>[012x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/(?P<a>[0])/(?P<b>[0])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', f7, name='f7'),
    url(r'^b9/(?P<f7tp>im9)(?P<l8p>[012x]?)/-(?P<tp>.+\.(gif|jpg|jpeg|png))-/(?P<a>[0])/(?P<b>[0])/(?P<c>\d+)/(?P<d>[01x])/(?P<e>[01x])/$', b9, name='b9'),
]
