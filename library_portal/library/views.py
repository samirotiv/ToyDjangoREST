from django.shortcuts import render,redirect
from .models import Book, Customer, Librarian
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views import generic
from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
	
	template_name = 'library/index.html'
	context_object_name = 'book_list'

	def get_queryset(self):
		return Book.objects.order_by('book_title')

class DetailView(generic.DetailView):

    model = Book
    template_name = 'library/detail.html'

def welcome(request):
	if request.user.is_authenticated() == True:
		return redirect('/library/index')
	return render(request,'library/welcome.html')

def login_page(request):
	return render(request,'library/login.html')

def register_page(request):
	return render(request,'library/register.html')

def registration_success(request,name):
	context={'name':name}
	return render(request,'library/registration_success.html',context) 

def register_func(request):
	u=User.objects.create_user(first_name=request.POST['first_name'],last_name=request.POST['last_name'],username=request.POST['user_name'],password=request.POST['password'])
	u.save()
	if request.POST['user_type']=="L":
		lib=Librarian(user=u)
		lib.save()
	elif request.POST['user_type']=="C":
		cust=Customer(user=u)
		cust.save()
	
	return HttpResponseRedirect(reverse('library:registration_success',args=(u.first_name,)))

def login_func(request):
	username=request.POST['user_name']
	password=request.POST['password']
	user=authenticate(username=username, password=password)
	if user is not None:
		login(request,user)
		return HttpResponseRedirect('/library/index')			
	else:
		return HttpResponse('Wrong username or password. <a href="/library/login">Try again</a>.')

def logout_func(request):
	logout(request)
	return redirect('/library/welcome')

def add_book_page(request):
	return render(request,'library/add_book.html')

def add_book_func(request):
	b=Book(book_title=request.POST['book_title'],publisher=request.POST['publisher'],author=request.POST['author'],date_added=timezone.now(),total_number=request.POST['total_num'])
	b.save()
	return redirect('/library/index')

def edit_book_page(request,book_id):
	book=Book.objects.get(pk=book_id)
	return render(request,'library/edit_book.html',{'book':book})

def edit_book_func(request,book_id):
	b=Book.objects.get(pk=book_id)
	b.book_title=request.POST['book_title']
	b.author=request.POST['author']
	b.publisher=request.POST['publisher']
	b.total_number=request.POST['total_num']
	b.save()
	return HttpResponseRedirect(reverse('library:detail',args=(book_id)))

def delete_book_page(request,book_id):
	book=Book.objects.get(pk=book_id)
	return render(request,'library/delete_book.html',{'book_id':book_id})

def delete_book_func(request,book_id):
	book=Book.objects.get(pk=book_id)
	book.delete()
	return redirect('/library/index')	

def request_book(request,book_id):
	book=Book.objects.get(pk=book_id)
	if request.user.customer.book_borrowed is not None:
		return HttpResponse("You have already requested one book! You can't request more till you return what you have taken!!")
	else:
		book.total_lent+=1
		book.save()
		request.user.customer.book_borrowed=book
		request.user.customer.save()
		return HttpResponseRedirect(reverse('library:detail',args=(book_id)))

def return_book(request,book_id):
	book=Book.objects.get(pk=book_id)
	if request.user.customer.book_borrowed == book:
		book.total_lent-=1
		book.save()
		request.user.customer.book_borrowed=None
		request.user.customer.save()
		return HttpResponseRedirect(reverse('library:detail',args=(book_id)))	



