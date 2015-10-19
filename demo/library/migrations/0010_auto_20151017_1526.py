# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20151017_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('person_that_borrowed_it', models.CharField(max_length=100)),
                ('book_that_was_borrowed', models.CharField(max_length=100)),
                ('no_of_copies', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Borrowed',
        ),
    ]
