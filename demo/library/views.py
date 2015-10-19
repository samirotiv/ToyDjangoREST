from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book,Borrower,LibraryUser
from .forms import LoginForm,RegisterForm,OrderForm,RequestForm
from django.views.generic import ListView
from rest_framework import generics
from library.models import Book
from library.serializers import BookSerializer,LibraryUserSerializer
from rest_framework import permissions

class LibraryUserList(generics.ListAPIView):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer


class LibraryUserDetail(generics.RetrieveAPIView):
    lookup_field='username'    
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
    
class SerialBookList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SerialBookDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'title'    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
'''This is the class based view version.
class BookList(APIView):
    """
    List all books, or creates a new book.
    """
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''        
''' This is the function based view version.
@api_view(['GET', 'POST']) #Use this decorator for function based views
def book_list(request,format=None):
    """
    List all books.
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])# book_detail is a function based view as well, so use the @api_view connector
def book_detail(request, book_title,format=None):
    """
    Retrieve, update or delete a book.
    """
    try:
        book = Book.objects.get(title=book_title)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)#Note the use of request.data here. This handles not only
        #JSON, but any incoming data format.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
'''        
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

