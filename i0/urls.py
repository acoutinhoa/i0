from django.conf.urls import url
from i0.views import *

urlpatterns = [
    url(r'^$', index0f, name='index0f'),
    # sites
    url(r'^bg/a=(?P<a>[0-2])/b=(?P<b>bg)/c=(?P<c>([01r]{3}|r|pb|rgb|piet))/d=(?P<d>[0-1])/$', bg, name='bg'),
    url(r'^f7/a=(?P<a>[0-2])/b=(?P<b>bg)/c=(?P<c>([01r]{3}|r|pb|rgb|piet))/d=(?P<d>[0-1])/$', f7, name='f7'),
    url(r'^f7/$', f70, name='f70'),
]
