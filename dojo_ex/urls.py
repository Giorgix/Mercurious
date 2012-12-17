from django.conf.urls import patterns, url

from dojo_ex import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
