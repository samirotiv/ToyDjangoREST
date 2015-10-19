# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ForeignKey(blank=True, to='portal.Author', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'Book added date', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
