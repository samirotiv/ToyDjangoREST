# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20150923_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='books_list',
        ),
        migrations.AddField(
            model_name='library',
            name='books_list',
            field=models.ManyToManyField(to='portal.Book', null=True, blank=True),
        ),
    ]
