__author__ = 'Admin'

from django.conf.urls import patterns, url
from lessons import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^logs/', views.log_table, name='logs'),
    url(r'^edit/person/(?P<skype>[\w-]+)/', views.person_editing, name='person_editing')
)