from django.conf.urls import url
from f7.views import *

urlpatterns = [
    url(r'^f7/$', f7, {'t2':'', 'v4r':'', 'l8p':'', 'f7':'', 'b9':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='f7'),
    url(r'^b9/$', b9, {'t2':'', 'v4r':'', 'l8p':'', 'f7':'', 'b9':'', 'a':'', 'b':'', 'c':'', 'd':'', 'e':'', }, name='b9'),
    url(r'^f7/t2=(?P<t2>(d0t|qd2|pi3t)?)/v4r=(?P<v4r>([01x]{3}|x|pb|rgb|piet|cmyx|def)?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>[01x]?)/c=(?P<c>(\d+)?)/d=(?P<d>([01x]([0-8]|x)?)?)/e=(?P<e>[01x]?)/$', f7, name='f7'),
    url(r'^b9/t2=(?P<t2>(d0t|qd2|pi3t)?)/v4r=(?P<v4r>([01x]{3}|x|pb|rgb|piet|cmyx|def)?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>[01x]?)/c=(?P<c>(\d+)?)/d=(?P<d>([01x]([0-8]|x)?)?)/e=(?P<e>[01x]?)/$', b9, name='b9'),
    url(r'^f7/t2=(?P<t2>(im9)?)/v4r=(?P<v4r>(0|1|(.+\.(gif|jpg|jpeg|png)))?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>([0-8]|x)?)/c=(?P<c>(\d+)?)/d=(?P<d>([01x]([0-8]|x)?)?)/e=(?P<e>[01x]?)/$', f7, name='f7'),
    url(r'^b9/t2=(?P<t2>(im9)?)/v4r=(?P<v4r>(0|1|(.+\.(gif|jpg|jpeg|png)))?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>([0-8]|x)?)/c=(?P<c>(\d+)?)/d=(?P<d>([01x]([0-8]|x)?)?)/e=(?P<e>[01x]?)/$', b9, name='b9'),
]
