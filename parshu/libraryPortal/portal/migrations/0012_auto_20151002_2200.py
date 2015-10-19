# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_library_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='books_list',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]
