# -*- coding: utf-8 -*-
import random
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import resolve
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from django.test import TestCase
from django.test import Client
from django.utils import timezone
import time
from lessons.models import Person


def create_person(name, phone, address, email, skype):
    dob = timezone.now()
    return Person.objects.create(name=name, dob=dob, phone=phone,
                                 address=address, email=email, skype=skype)


class MainPageTest(TestCase):

    def test1(self):
        c = Client()
        create_person(name=u'Кот', phone='123', address='Santa Monica',
                      email='kokoko@k.com', skype='GiantCat')
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Кот", response.content)


class MiddlewareTest(TestCase):

    def middleware_test(self):
        c = Client()
        request_url = '/kokoko'+str(timezone.now())
        response = c.get(request_url)
        log_response = c.get(resolve('logs'))
        self.assertIn(request_url, log_response.content)


class ContextProcessorTest(TestCase):

    def context_processor_test(self):
        c = Client()
        response = c.get('/')
        self.assertIn(settings.STATIC_ROOT, response.content)


class EditingLinkTest(TestCase):

    def link_test(self):
        instance = create_person(name=u'Кот', phone='123', address='Santa Monica',
                                 email='kokoko@k.com', skype='GiantCat')
        app = ContentType.objects.get_for_model(instance).app_label
        model = ContentType.objects.get_for_model(instance).model
        inst_pk = str(instance.pk)
        c = Client()
        response = c.get('/')
        link = '127.0.0.1:8000/admin/'+app+'/'+model+'/'+inst_pk
        self.assertIn(link, response.content)


"""
class MySeleniumTests(LiveServerTestCase):
    #fixtures = ['initial_data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(MySeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_main(self):
        create_person(name=u'Кот', phone='123', address='Santa Monica',
                      email='kokoko@k.com', skype='GiantCat')
        self.selenium.get('http://127.0.0.1:8081/')
        self.assertIn(u"Кот", self.selenium.page_source)

    def test_log(self):
        request_url = 'kokoko'+''.join([random.choice("1234567890") for x in range(10)])
        self.selenium.get('http://127.0.0.1:8081/' + request_url)
        self.selenium.get("http://127.0.0.1:8081/lessons/logs")
        self.assertIn(request_url, self.selenium.page_source)
        """
