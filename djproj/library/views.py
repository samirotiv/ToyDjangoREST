from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book,Borrower,LibraryUser
from .forms import LoginForm,RegisterForm,OrderForm,RequestForm
from django.views.generic import ListView

class BookList(ListView):
    model = Book
    queryset = Book.objects.order_by('author')
    def get_queryset(self):
        return Book.objects.order_by(self.args[0])   
# Create your views here.

def get_name(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:            
                userchk = LibraryUser.objects.get(
                username = form.cleaned_data['user_name'])
            except:
                return HttpResponseRedirect("/library/register")
            try:            
                passchk = LibraryUser.objects.get(
            password = form.cleaned_data['passwd'])
            except:
                return HttpResponseRedirect("/library/register")
            if userchk==passchk:
                return HttpResponseRedirect("/library/welcome/%s" % form.cleaned_data['user_name'])            
    else:
        form = LoginForm()
    return render(request, 'name.html', {'form': form})
    
def welcome(request,username):
    name = username
    user_object = LibraryUser.objects.get(username=name)
    if user_object.usertype=='C':
            return HttpResponseRedirect("/library/pickordering/%s" % name)

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name']
            pwd = form.cleaned_data['passwd']
            utype = form.cleaned_data['usertype']
            l = LibraryUser(username=name,password=pwd,usertype=utype)
            l.save()
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})    

def pick_order(request,username):
    customer_sort_form = OrderForm(prefix="ord")
    customer_borrow_form = RequestForm(prefix="bor")
    if request.method=='POST':
        customer_sort_form = OrderForm(request.POST,prefix="ord")
        customer_borrow_form = RequestForm(request.POST,prefix="bor")
        if 'order' in request.POST:
            if customer_sort_form.is_valid():
                method = customer_sort_form.cleaned_data['order']
                return HttpResponseRedirect("/library/books/%s" % method)    
        elif 'askforbooks' in request.POST:
            if customer_borrow_form.is_valid():
                book_title = customer_borrow_form.cleaned_data['title']
                no_of_copies = customer_borrow_form.cleaned_data['copies_required']
                return HttpResponseRedirect("/library/getbooks/%s/%s/%d" % (username,book_title,no_of_copies))
    else:
        customer_sort_form = OrderForm(prefix="ord")
        customer_borrow_form = RequestForm(prefix="bor")
    return render(request,'pickorder.html',
                  {'customer_sort_form':customer_sort_form,'customer_borrow_form':customer_borrow_form})
    
def borrow_books(request,user_name,book_title,no_of_copies):
    b = Book.objects.get(title=book_title)
    copies = int(no_of_copies)    
    if (b.count-copies)>=0:
        b.count=b.count-copies
        b.save()        
        bo=Borrower(person_that_borrowed_it=user_name,book_that_was_borrowed=book_title,no_of_copies=copies)
        bo.save()        
        return HttpResponse("Your book has been borrowed successfully!")
    else:
        return HttpResponse("Invalid book selected. Please go back and choose again.")
    