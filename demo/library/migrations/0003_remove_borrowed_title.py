# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20151013_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed',
            name='title',
        ),
    ]
