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
]
