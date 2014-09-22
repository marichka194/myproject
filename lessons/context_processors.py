from django.conf import settings

__author__ = 'Admin'


def static(request):
    return {'STATIC_ROOT': settings.STATIC_ROOT}


def databases(request):
    databases_dict = {'default': settings.DATABASES['default']}
    return databases_dict


def languages(request):
    return {'languages':settings.LANGUAGE_CODE}
