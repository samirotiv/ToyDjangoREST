# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authorName', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['authorName'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200, null=True, blank=True)),
                ('date', models.DateTimeField(null=True, verbose_name=b'Book added date', blank=True)),
                ('noBooks', models.IntegerField(default=0)),
                ('authors', models.ManyToManyField(to='portal.Author')),
            ],
            options={
                'ordering': ['-title', 'publisher', 'noBooks'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userType', models.BooleanField(default=False, choices=[(True, b'Librarian'), (False, b'Customer')])),
                ('currentBook', models.ForeignKey(blank=True, to='portal.Book', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
