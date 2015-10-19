# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20151017_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='book_that_was_borrowed',
            field=models.CharField(max_length=100),
        ),
    ]
