from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
# Create your models here.

class Book(models.Model):
	book_title=models.CharField(max_length=200)
	publisher=models.CharField(max_length=200)
	author=models.CharField(max_length=200)
	date_added=models.DateTimeField('Date Added')
	total_number=models.IntegerField(default=0)
	total_lent=models.IntegerField(default=0)
	def available(self):
		return self.total_lent<self.total_number
	def __unicode__(self):
		return self.book_title

	class Meta:
		permissions=(("request_book","customer can request books"),("return_book","customer can return book"))

class Customer(models.Model):
	user=models.OneToOneField(User)
	book_borrowed=models.ForeignKey(Book,null=True)
	user.user_permissions=["request_book","return_book"]
	def __unicode__(self):
		return self.user.first_name
	
class Librarian(models.Model):
	user=models.OneToOneField(User)
	user.user_permissions=["add_book","change_book","delete_book"]
	def __unicode__(self):
		return self.user.first_name
	