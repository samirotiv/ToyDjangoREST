# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_delete_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(related_name='books', default=b'Varun', to='library.LibraryUser'),
        ),
    ]
