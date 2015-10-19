# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_borrowed_book_that_was_borrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryuser',
            name='password',
            field=models.CharField(max_length=100, default='imanidiot'),
        ),
    ]
