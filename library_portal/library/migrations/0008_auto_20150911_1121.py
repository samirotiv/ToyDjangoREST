# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20150911_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('request_book', 'customer can request books'), ('return_book', 'customer can return book'), ('add_book', 'can add books'), ('edit_book', 'can edit books'), ('delete_book', 'can delete books'))},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='librarian',
            options={},
        ),
    ]