from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),

    url(r'^vote/$', views.vote, name='vote'),
    url(r'^test/$', views.test, name='test'),
)
