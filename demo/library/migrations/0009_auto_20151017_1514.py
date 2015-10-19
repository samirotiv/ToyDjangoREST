# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20151017_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
