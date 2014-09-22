# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_hui'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hui1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
