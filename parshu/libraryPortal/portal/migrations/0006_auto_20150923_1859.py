# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20150923_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userType',
            field=models.BooleanField(default=False, choices=[(True, b'Librarian'), (False, b'Customer')]),
        ),
    ]
