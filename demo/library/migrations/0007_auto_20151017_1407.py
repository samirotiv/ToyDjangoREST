# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20151016_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='person_that_borrowed_it',
            field=models.CharField(max_length=100),
        ),
    ]
