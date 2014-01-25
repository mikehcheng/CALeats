from django.conf.urls import patterns, url

from caleats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^vote/$', views.vote),
    url(r'^(?P<hall>\S+)/$', views.detail, name='detail'),
)