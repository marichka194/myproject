# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_hui1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hui',
        ),
        migrations.DeleteModel(
            name='Hui1',
        ),
    ]
