from django.conf import settings

__author__ = 'Admin'


def settings_def(request):
    return {'settings': settings}

"""
def databases(request):
    databases_dict = {'default': settings.DATABASES['default']}
    return databases_dict


def languages(request):
    return {'languages': settings.LANGUAGE_CODE}
"""