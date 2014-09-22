# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u0424\u0418\u041e')),
                ('dob', models.DateField(verbose_name='\u0424\u0418\u041e')),
                ('phone', models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('address', models.TextField(verbose_name='\u0424\u0418\u041e')),
                ('email', models.EmailField(max_length=75, verbose_name='\u0424\u0418\u041e')),
                ('skype', models.CharField(max_length=20, verbose_name='\u0424\u0418\u041e')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
