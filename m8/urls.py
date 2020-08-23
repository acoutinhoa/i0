from django.conf.urls import url
from m8 import views

urlpatterns = [
    url(r'^$', views.m8, name='m8'),
]
