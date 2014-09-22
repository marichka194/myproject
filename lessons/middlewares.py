# -*- coding: utf-8 -*-

from lessons.models import Log

__author__ = 'Admin'


class LogRequestMiddleware(object):

    def process_request(self, request):
        method = request.method
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        #url = request.META['SERVER_NAME'].decode('cp1251')+request.META['SERVER_PORT']+request.path
        url = request.META.get('HTTP_HOST', '')+request.path
        new_log = Log.objects.create(method=method, url=url, user_agent=user_agent)