# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20150928_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='books_list',
            field=models.ManyToManyField(to='portal.Book'),
        ),
    ]
