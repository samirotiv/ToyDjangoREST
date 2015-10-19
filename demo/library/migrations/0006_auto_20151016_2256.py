# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_libraryuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraryuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='libraryuser',
            name='password',
            field=models.CharField(serialize=False, max_length=100, primary_key=True, default='imanidiot'),
        ),
    ]
