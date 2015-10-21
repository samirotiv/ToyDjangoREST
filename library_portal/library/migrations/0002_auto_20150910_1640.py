# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='book_borrowed',
            field=models.ForeignKey(to='library.Book', null=True),
        ),
    ]
