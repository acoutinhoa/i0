from django.conf.urls import url
from i0.views import *

urlpatterns = [
    url(r'^$', index0f, name='index0f'),
    # sites
    url(r'^bg/(?P<c>[0-3])/(?P<d>[0-2])/(?P<rl>[0-2])/$', bg, name='bg'),
    url(r'^f7bg/c=(?P<c>[0-3])/d=(?P<d>[0-2])/rl=(?P<rl>[0-2])/$', f7bg, name='f7bg'),
    url(r'^f7bg/$', f7bg0, name='f7bg0'),
]
