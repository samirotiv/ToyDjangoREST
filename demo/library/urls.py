# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 23:36:18 2015

@author: HP-PC
"""
from django.conf.urls import url,include
from library.views import BookList
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    url(r'^$',views.get_name,name = 'get_name'),
    url(r'^welcome/(?P<username>\D+)/$'
    , views.welcome, name='welcome'),
    url(r'^register/$',views.register,name = 'register'),
    url(r'^pickordering/(?P<username>\D+)/$',views.pick_order,name = 'pickorder'),
    url(r'^books/(\D+)$', BookList.as_view(),
                  name='book_list'),
    url(r'^getbooks/(?P<user_name>\D+)/(?P<book_title>\D+)/(?P<no_of_copies>\d+)$'
    ,views.borrow_books,name = 'borrow_books'),
    url(r'^serialbooks/$', views.SerialBookList.as_view()),
    url(r'^serialbooks/(?P<title>\D+)/$', views.SerialBookDetail.as_view(),name='book-detail'),
    url(r'^users/$', views.LibraryUserList.as_view(),name='libraryuser-list'),
    url(r'^users/(?P<username>\D+)/$', views.LibraryUserDetail.as_view(),name='libraryuser-detail'),              
]

urlpatterns = format_suffix_patterns(urlpatterns)