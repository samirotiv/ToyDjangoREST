# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20151017_1542'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
