# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowed',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('usertype', models.CharField(max_length=20, choices=[('C', 'Customer'), ('L', 'Librarian')], default='C')),
            ],
        ),
        migrations.AddField(
            model_name='borrowed',
            name='person_that_borrowed_it',
            field=models.ForeignKey(to='library.Users'),
        ),
    ]
