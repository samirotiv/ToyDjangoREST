# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 23:36:18 2015

@author: HP-PC
"""
from django.conf.urls import url
from library.views import BookList
from . import views
urlpatterns = [
    url(r'^$',views.get_name,name = 'get_name'),
    url(r'^welcome/(?P<username>\D+)/$'
    , views.welcome, name='welcome'),
    url(r'^register/$',views.register,name = 'register'),
    url(r'^pickordering/(?P<username>\D+)/$',views.pick_order,name = 'pickorder'),
    url(r'^books/(\D+)$', BookList.as_view(),
                  name='book_list'),
    url(r'^getbooks/(?P<user_name>\D+)/(?P<book_title>\D+)/(?P<no_of_copies>\d+)$',views.borrow_books,name = 'borrow_books'),              
]
