from django.db import models
# Create your models here.
class LibraryUser(models.Model):
    def __str__(self):
        return self.username
    CUSTOMERS = 'C'
    LIBRARIANS = 'L'    
    USER_TYPE_CHOICES = (
        (CUSTOMERS, 'Customer'),
        (LIBRARIANS, 'Librarian'),
    )
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100,default="imanidiot",primary_key=True)
    usertype = models.CharField(max_length=20,
            choices=USER_TYPE_CHOICES,default=CUSTOMERS)

class Borrower(models.Model):
    def __str__(self):
        return self.person_that_borrowed_it
    person_that_borrowed_it = models.CharField(max_length=100)
    book_that_was_borrowed = models.CharField(max_length=100)
    no_of_copies = models.IntegerField()

class Book(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now=False,auto_now_add=True)

