# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20150928_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
