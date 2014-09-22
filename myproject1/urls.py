from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from lessons import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

