# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20150910_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('request_book', 'customer can request books'), ('return_book', 'customer can return book'))},
        ),
        migrations.AlterModelOptions(
            name='librarian',
            options={'permissions': (('add_book', 'can add books'), ('edit_book', 'can edit books'), ('delete_book', 'can delete books'))},
        ),
    ]
