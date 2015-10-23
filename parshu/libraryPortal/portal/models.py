import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    authorName = models.CharField(max_length=200)
    date_added = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return self.authorName

    class Meta:
           ordering = ['authorName']

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True, null=True)
    date = models.DateTimeField('Book added date', blank=True, null=True)
    noBooks = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
           ordering = ['-title', 'publisher', 'noBooks']

USER_CHOICES = ((True, 'Librarian'), (False, 'Customer'))

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # additional attributes
    currentBook = models.ForeignKey(Book, blank=True, null=True )
    userType = models.BooleanField(choices=USER_CHOICES,  default=False )

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
