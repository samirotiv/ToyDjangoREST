# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20150910_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 11, 38, 51, 693962, tzinfo=utc), verbose_name=b'Date Added'),
        ),
    ]
