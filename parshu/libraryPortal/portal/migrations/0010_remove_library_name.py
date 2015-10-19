# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_library_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='name',
        ),
    ]
