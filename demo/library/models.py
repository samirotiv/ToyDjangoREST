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
    owner = models.ForeignKey('library.LibraryUser', default='Varun',related_name='books')
    '''Note that in the above line, the default should actually be a LibraryUser object, not a string.
    However, the built in ModelSerializer that we use to serialize this class cannot handle LibraryUser as a datatype.
    My workaround is that I give a nonsensical default, Varun in this case,and then open a Python shell and set the 
    default as a LibraryUser manually. I haven't modified any of the old forms for this.    
    '''
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now=False,auto_now_add=True)

