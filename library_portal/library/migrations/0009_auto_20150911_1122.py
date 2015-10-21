# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20150911_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('request_book', 'customer can request books'), ('return_book', 'customer can return book'))},
        ),
    ]
