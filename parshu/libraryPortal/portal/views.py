from django.shortcuts import render , render_to_response , get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.core import serializers

from portal.forms import UserForm, UserProfileForm, AddBookForm, AuthorForm
from portal.models import UserProfile , Book , Author

def index(request):
    context = RequestContext(request)
    return render_to_response('portal/index.html', {}, context)

def registerUser(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user  = user

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'portal/registration.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            if user.userprofile.userType:
                return HttpResponseRedirect('/portal')
            else:
                return HttpResponseRedirect('/portal')
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponseRedirect('/portal/login')

    else:
        return render_to_response('portal/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/portal')

@login_required
def addBook(request):
    context = RequestContext(request)
    if request.method == 'POST' :
        form = AddBookForm(data=request.POST)
        if form.is_valid():
            form.save()
            m = 'saved'
        else:
            m = 'failed'
    else:
        form = AddBookForm()
        m = ''

    return render_to_response('portal/generic.html' ,
            {'heading' : "Add Book" , 'message' : m , 'form' : form }  , context  )


@login_required
def addAuthor(request):
    context = RequestContext(request)
    if request.method == 'POST' :
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            m = 'saved'
        else:
            m = 'failed'
    else:
        form = AuthorForm()
        m = ''

    return render_to_response('portal/generic.html' ,
            {'heading' : "Add Author" , 'message' : m , 'form' : form }  , context  )

@login_required
def editBook(request , primaryKey):
    context = RequestContext(request)
    book = Book.objects.get(pk=primaryKey)
    if request.method == 'POST' :
        form = AddBookForm(data=request.POST , instance = book)
        if form.is_valid():
            form.save()
            m = 'saved'
        else:
            m = 'failed'
    else:
        form = AddBookForm(instance = book)
        m = ''

    return render_to_response('portal/generic.html' ,
            {'heading' : "Edit Book" , 'message' : m , 'form' : form }  , context  )

@login_required
def editAuthor(request , primaryKey):
    context = RequestContext(request)
    author = Author.objects.get(pk=primaryKey)
    if request.method == 'POST' :
        form = AuthorForm(data=request.POST , instance = author)
        if form.is_valid():
            form.save()
            m = 'saved'
        else:
            m = 'failed'
    else:
        form = AuthorForm(instance = author)
        m = ''

    return render_to_response('portal/generic.html' ,
            {'heading' : "Edit Author" , 'message' : m , 'form' : form }  , context  )


@login_required
def deleteBook(request , primaryKey):
    context = RequestContext(request)
    book = Book.objects.get(pk=primaryKey)
    book.delete()
    m = "Done"
    return render_to_response('portal/generic.html' ,
            {'heading' : "Delete Book" , 'message' : m , 'form' : '' }  , context  )


@login_required
def borrowBook(request , primaryKey):
    context = RequestContext(request)
    book = Book.objects.get(pk=primaryKey)

    request.user.currentBook = book
    request.user.save()

    m = request.user.currentBook.title
    return render_to_response('portal/generic.html' ,
            {'heading' : "Borrow Book" , 'message' : m , 'form' : '' }  , context  )

@login_required
def returnBook(request , primaryKey):
    context = RequestContext(request)
    book = Book.objects.get(pk=primaryKey)

    request.user.currentBook.null = True;

    m = request.user.username
    return render_to_response('portal/generic.html' ,
            {'heading' : "Return Book" , 'message' : m , 'form' : '' }  , context  )

@login_required
def librarian(request , sortby ):
    context = RequestContext(request)
    bookList = Book.objects.all()
    authorList = Author.objects.all()

    if sortby == "title" :
        bookList = bookList.order_by('title')
    elif sortby == "publisher" :
        bookList = bookList.order_by('publisher')
    elif sortby == "noBooks" :
        bookList = bookList.order_by('noBooks')

    return render_to_response('portal/librarian.html' ,
            {'heading' : "Librarian Profile" , 'bookList' : bookList, 'authorList':authorList }  , context  )

@login_required
def customer(request ):
    context = RequestContext(request)
    bookList = Book.objects.all()
    authorList = Author.objects.all()
    # currentBook = request.user.currentBook
    return render_to_response('portal/customer.html' ,
            {'heading' : "Customer Profile" , 'bookList' : bookList, 'authorList':authorList  }  , context  )
