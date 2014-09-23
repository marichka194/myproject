from string import split
from django.contrib.contenttypes.models import ContentType
from django import template
from django.core.urlresolvers import reverse

__author__ = 'Admin'

register = template.Library()


@register.filter(is_safe=True)
def ed_link(instance):
    app = str(ContentType.objects.get_for_model(instance).app_label)
    model = ContentType.objects.get_for_model(instance).model
    inst_pk = str(instance.pk)
    link = reverse('admin:app_list', kwargs={'app_label': app})+model+'/'+inst_pk+'/'
    return link


@register.filter(is_safe=True)
def splitter(value, split_symbol):
    return split(s=str(value), sep=split_symbol)


@register.simple_tag
def edit_link(instance):
    app = str(ContentType.objects.get_for_model(instance).app_label)
    model = ContentType.objects.get_for_model(instance).model
    inst_pk = str(instance.pk)
    link = reverse('admin:app_list', kwargs={'app_label': app})+model+'/'+inst_pk+'/'
    return link

