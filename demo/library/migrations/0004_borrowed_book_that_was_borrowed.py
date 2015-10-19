# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_borrowed_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='book_that_was_borrowed',
            field=models.ForeignKey(to='library.Book', default=1),
        ),
    ]
