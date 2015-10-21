from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^index/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^register/$', views.register_page, name='register'),
    url(r'^registration_success/(?P<name>\w+)/$', views.registration_success, name='registration_success'),
    url(r'^register_func/$', views.register_func, name='register_func'),
    url(r'^login_func/$', views.login_func, name='login_func'),
    url(r'^logout/$', views.logout_func, name='logout'),
    url(r'^index/add_book/$',views.add_book_page,name="add_book_page"),
    url(r'^index/add_book_func/$',views.add_book_func,name="add_book_func"),
    url(r'^index/(?P<book_id>[0-9]+)/edit_book_page/$',views.edit_book_page,name="edit_book_page"),
    url(r'^index/(?P<book_id>[0-9]+)/edit_book_func/$',views.edit_book_func,name="edit_book_func"),
    url(r'^index/(?P<book_id>[0-9]+)/delete_book_page/$',views.delete_book_page,name="delete_book_page"),
    url(r'^index/(?P<book_id>[0-9]+)/delete_book_func/$',views.delete_book_func,name="delete_book_func"),
    url(r'^index/(?P<book_id>[0-9]+)/request_book/$',views.request_book,name="request_book"),
    url(r'^index/(?P<book_id>[0-9]+)/return_book/$',views.return_book,name="return_book"),
]
