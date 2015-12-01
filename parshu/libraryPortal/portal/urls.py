from django.conf.urls import url,patterns , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',

    # url(r'^$', views.index, name='index'),
    #url(r'^addbook/$', name='addBook'),
    url(r'^book/$', views.SerialBookList.as_view(), name='book'),
    url(r'^author/$', views.SerialAuthorList.as_view(), name='Author'),
    url(r'^author/updates/$',views.SerialUpdateAuthorList.as_view(),name='Update'),
    url(r'^author/books/$', views.SerialSendBookListOfAuthor.as_view(), name='AuthorList'),
    
    # url(r'^editbook/(?P<primaryKey>[0-9]+)/$', views.editBook, name='editBook'),
    # url(r'^deletebook/(?P<primaryKey>[0-9]+)/$', views.deleteBook, name='deleteBook'),
    # url(r'^borrowbook/(?P<primaryKey>[0-9]+)/$', views.borrowBook, name='borrowBook'),
    # url(r'^returnbook/(?P<primaryKey>[0-9]+)/$', views.returnBook, name='returnBook'),
    # url(r'^editauthor/(?P<primaryKey>[0-9]+)/$', views.editAuthor, name='editAuthor'),
    url(r'^registration/$',views.registerUser, name='registration'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^customer/$',views.customer, name='customer'),

    url(r'^librarian/(?P<sortby>[A-Za-z]+)/$', views.librarian, name='librarian'),


    url(r'^$', views.UserChatView.as_view(), name='user_chat'),

) + staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)