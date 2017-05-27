from django.conf.urls import url
from f7 import views

urlpatterns = [
    url(r'^$', views.f7m3, name='f7m3'),
    url(r'^m3/t2=(?P<t2>(.+)?)/v4r=(?P<v4r>(.+)?)/l8p=(?P<l8p>(.+)?)/f7=(?P<f7>(.+)?)/b9=(?P<b9>(.+)?)/a=(?P<a>(.+)?)/b=(?P<b>(.+)?)/c=(?P<c>(.+)?)/d=(?P<d>(.+)?)/$', views.f7m3, name='f7m3'),
    url(r'^m3/f7/t2=(?P<t2>(.+)?)/v4r=(?P<v4r>(.+)?)/l8p=(?P<l8p>(.+)?)/f7=(?P<f7>(.+)?)/b9=(?P<b9>(.+)?)/a=(?P<a>(.+)?)/b=(?P<b>(.+)?)/c=(?P<c>(.+)?)/d=(?P<d>(.+)?)/$', views.m3, name='m3'),

    url(r'^b9/$', views.b9, name='b9'),
    url(r'^b9/t2=(?P<t2>(.+)?)/v4r=(?P<v4r>(.+)?)/l8p=(?P<l8p>(.+)?)/f7=(?P<f7>(.+)?)/b9=(?P<b9>(.+)?)/a=(?P<a>(.+)?)/b=(?P<b>(.+)?)/c=(?P<c>(.+)?)/d=(?P<d>(.+)?)/(?P<n>\d+)/$', views.b9, name='b9'),
    url(r'^b9/t2=(?P<t2>(.+)?)/v4r=(?P<v4r>(.+)?)/l8p=(?P<l8p>(.+)?)/f7=(?P<f7>(.+)?)/b9=(?P<b9>(.+)?)/a=(?P<a>(.+)?)/b=(?P<b>(.+)?)/c=(?P<c>(.+)?)/d=(?P<d>(.+)?)/$', views.b9, name='b9'),

    url(r'^f7/$', views.f7, name='f7'),
    url(r'^t2=(?P<t2>(.+)?)/v4r=(?P<v4r>(.+)?)/l8p=(?P<l8p>(.+)?)/f7=(?P<f7>(.+)?)/b9=(?P<b9>(.+)?)/a=(?P<a>(.+)?)/b=(?P<b>(.+)?)/c=(?P<c>(.+)?)/d=(?P<d>(.+)?)/(?P<n>\d+)/$', views.f7, name='f7'),
    url(r'^t2=(?P<t2>(.+)?)/v4r=(?P<v4r>(.+)?)/l8p=(?P<l8p>(.+)?)/f7=(?P<f7>(.+)?)/b9=(?P<b9>(.+)?)/a=(?P<a>(.+)?)/b=(?P<b>(.+)?)/c=(?P<c>(.+)?)/d=(?P<d>(.+)?)/$', views.f7, name='f7'),

    url(r'^.+/$', views.f7, {'t2':'ka8s',}, name='f7'),

    # url(r'^m3/$', views.m3, name='m3'),
    # url(r'^f7/$', views.f7m3, name='f7m3'),
    # url(r'^f7/$', f7, {'t2':'', 'v4r':'', 'l8p':'', 'f7':'', 'b9':'', 'a':'', 'b':'', 'c':'', 'd':'', 'n':'0'}, name='f7'),
    # url(r'^b9/$', views.b9, {'t2':'', 'v4r':'', 'l8p':'', 'f7':'', 'b9':'', 'a':'', 'b':'', 'c':'', 'd':'', 'n':'0'}, name='b9'),
    # url(r'^f7/t2=(?P<t2>(d0t|qd2|pi3t)?)/v4r=(?P<v4r>([01x]{3}|x|pb|rgb|piet|cmyx|def)?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>[01x]?)/c=(?P<c>[01x]?)/d=(?P<d>([01x]([0-8]|x)?)?)/(?P<n>\d+)/$', views.f7, name='f7'),
    # url(r'^f7/t2=(?P<t2>(d9d)?)/v4r=(?P<v4r>([01x]{3}|x|pb|rgb|piet|cmyx|def)?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>([012x]{2})?)/c=(?P<c>[01x]?)/d=(?P<d>([01x]([0-8]|x)?)?)/(?P<n>\d+)/$', views.f7, name='f7'),
    # url(r'^f7/t2=(?P<t2>(im9)?)/v4r=(?P<v4r>(.+\.(gif|jpg|jpeg|png))?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>([0-8]|x)?)/c=(?P<c>[01x]?)/d=(?P<d>([01x]([0-8]|x)?)?)/(?P<n>\d+)/$', views.f7, name='f7'),
    # url(r'^f7/t2=(?P<t2>ka8s)/v4r=(?P<v4r>)/l8p=(?P<l8p>)/f7=(?P<f7>)/b9=(?P<b9>)/a=(?P<a>)/b=(?P<b>)/c=(?P<c>)/d=(?P<d>)/(?P<n>\d+)/$', views.f7, name='f7'),
    # url(r'^b9/t2=(?P<t2>(d0t|qd2|pi3t)?)/v4r=(?P<v4r>([01x]{3}|x|pb|rgb|piet|cmyx|def)?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>[01x]?)/c=(?P<c>[01x]?)/d=(?P<d>([01x]([0-8]|x)?)?)/(?P<n>\d+)/$', views.b9, name='b9'),
    # url(r'^b9/t2=(?P<t2>(d9d)?)/v4r=(?P<v4r>([01x]{3}|x|pb|rgb|piet|cmyx|def)?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>([012x]{2})?)/c=(?P<c>[01x]?)/d=(?P<d>([01x]([0-8]|x)?)?)/(?P<n>\d+)/$', views.b9, name='b9'),
    # url(r'^b9/t2=(?P<t2>(im9)?)/v4r=(?P<v4r>(.+\.(gif|jpg|jpeg|png))?)/l8p=(?P<l8p>[012x]?)/f7=(?P<f7>[012]?)/b9=(?P<b9>[01]?)/a=(?P<a>[01x]?)/b=(?P<b>([0-8]|x)?)/c=(?P<c>[01x]?)/d=(?P<d>([01x]([0-8]|x)?)?)/(?P<n>\d+)/$', views.b9, name='b9'),
    # url(r'^b9/t2=(?P<t2>ka8s)/v4r=(?P<v4r>\?)/l8p=(?P<l8p>\?)/f7=(?P<f7>\?)/b9=(?P<b9>\?)/a=(?P<a>\?)/b=(?P<b>\?)/c=(?P<c>\?)/d=(?P<d>\?)/(?P<n>\d+)/$', views.b9, name='b9'),
]
