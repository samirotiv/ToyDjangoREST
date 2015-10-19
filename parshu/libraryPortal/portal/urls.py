from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^addbook/$', views.addBook, name='addBook'),
    url(r'^addauthor/$', views.addAuthor, name='addAuthor'),
    url(r'^editbook/(?P<primaryKey>[0-9]+)/$', views.editBook, name='editBook'),
    url(r'^deletebook/(?P<primaryKey>[0-9]+)/$', views.deleteBook, name='deleteBook'),
    url(r'^borrowbook/(?P<primaryKey>[0-9]+)/$', views.borrowBook, name='borrowBook'),
    url(r'^returnbook/(?P<primaryKey>[0-9]+)/$', views.returnBook, name='returnBook'),
    url(r'^editauthor/(?P<primaryKey>[0-9]+)/$', views.editAuthor, name='editAuthor'),
    url(r'^registration/$',views.registerUser, name='registration'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^customer/$',views.customer, name='customer'),

    url(r'^librarian/(?P<sortby>[A-Za-z]+)/$', views.librarian, name='librarian'),

]
