# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20150910_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(verbose_name=b'Date Added'),
        ),
    ]
