from django.conf.urls import url
from e4 import views

urlpatterns = [
    url(r'^$', views.pdf, name='pdf'),
    url(r'^m=(?P<m>\d)/f=(?P<f>\d)/$', views.cartaz, name='cartaz'),
]
