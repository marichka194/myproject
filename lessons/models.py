# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType

from django.db import models
from django.db.models.signals import post_save, post_delete, class_prepared


class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'ФИО')
    dob = models.DateField(verbose_name=u'Дата рождения')
    phone = models.CharField(max_length=15, verbose_name=u'Телефон')
    address = models.TextField(verbose_name=u'Адрес')
    email = models.EmailField(verbose_name='E-mail')
    skype = models.CharField(max_length=20, verbose_name='Skype')


class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=5)
    url = models.URLField()
    user_agent = models.CharField(max_length=25)


class LogModel(models.Model):
    model = models.CharField(max_length=20)
    inst_pk = models.PositiveIntegerField()
    action = models.CharField(max_length=10)


def save_handler(sender, instance, created, **kwargs):
    if isinstance(instance, LogModel):
        return
    app = ContentType.objects.get_for_model(instance).app_label
    model = ContentType.objects.get_for_model(instance).model
    action = ''
    if created:
        action = 'created'
    else:
        action = 'edited'
    LogModel.objects.create(model=model, inst_pk=instance.pk, action=action)

post_save.connect(save_handler, Person)
post_save.connect(save_handler, Log)


def delete_handler(sender, instance, **kwargs):
    app = ContentType.objects.get_for_model(instance).app_label
    model = ContentType.objects.get_for_model(instance).model
    LogModel.objects.create(model=model, inst_pk=instance.pk, action='deleted')

post_delete.connect(save_handler, Person)
post_delete.connect(save_handler, Log)
