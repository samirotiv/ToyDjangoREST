#Introduction to Django-Websocket-Redis and 
#Sample app which returns the message posted by client via websocket.
-------------------------------------------------------
Do Check official docs for more clarity.!!

Introduction
============

Application servers such as Django is been developed without intention to create long living connections. Therefore these frameworks are not a good fit for web applications, which shall react on asynchronous events initiated by the server. One feasible solution for clients is Ajax request.However It produces a lot of traffic.

Web application written in Python usually use WSGI as the communication layer between the
webserver and themselves. WSGI is a stateless protocol which defines how to handle requests and
making responses in a simple way abstracted from the HTTP protocol, but by design it does not
support non-blocking requests.


The WSGI protocol can not support websockets
============================================

In Django, the web server accepts an incoming request, sets up a WSGI dictionary which then is
passed to the application server. There the HTTP headers and the payload is created and immediately
afterwards the request is finished and flushed to the client. 

As It is almost impossible to add support for long term connections, such as websockets, on top of the WSGI protocol specification. Therefore most websocket implementations go for another approach. The websocket connection is controlled by a service running side by side with the default application server. Here, a webserver with support for long term connections, dispatches the requests from the clients.


uWSGI and Redis as a message queue
==================================

And that is where `uWSGI offers websockets`_ right out of the box. With Redis_ as a message queue

an additional service – the Redis data server – runs side by side with Django. Websockets are bidirectional but their normal use case is to trigger server initiated events on the client. Although the other direction is possible, it can be handled much easier using Ajax


Scalability
-----------

One of the nice features of Redis is its infinite scalability. If one Redis server can't handle its
workload, interconnect it with another one and all events and messages are mirrored across this
network. Since **django-websocket-redis** can be deployed multiple times and as self-contained
Django applications, this configuration can scale infinitely, just interconnect the Redis servers
to each other.


Installation and Configuration
==============================

pip install 
pip install uWSGI


Running WebSocket for Redis
===========================
Start the redis server by typing  'redis-server'
After typing "redis-cli ping" on different terminal, it should repond with PONG as message means server is working perfectly.

Django with WebSockets for Redis as a stand alone uWSGI server
==============================================================

In this configuration the **uWSGI** server owns the main loop. To distinguish WebSockets from
normals requests, modified the Python starter module ``wsgi.py`` Check the file wsgi.py. 

--CODE 

This will answer, both Django and WebSocket requests on port 80 using HTTP. Here the modified
``application`` dispatches incoming requests depending on the URL on either a Django handler or
into the WebSocket's main loop.

Serving static files
--------------------

As In this configuration, we will not able to serve static files, because Django does not run in debug
mode and uWSGI does not know how to server deployed static files. Therefore in ``urls.py`` added
``staticfiles_urlpatterns`` to urlpatterns
=================================================================================================


...Sample APP
================================
IMP -- Using Websockets for Redis
=================================

Identification - Each websocket is identified by the part of the URL which follows the prefix
``/ws/`` which is specified using the configuration setting ``WEBSOCKET_URL`` in settings.py and can be changed to whatever is appropriate.

Client side
===========

The idea is to let a client subscribe for different channels, so that he only gets notified, when
a certain event happens on a channel he is interested in. Currently there are four such events,
*broadcast notification*, *user notification*, *group notification* and *session notification*.
Additionally, a client may declare on initialization, on which channels he wishes to publish a
message. The latter is not that important for a websocket implementation, because it can be achieved
otherwise, using the well known XMLHttpRequest (Ajax) methods.

Client JavaScript depending on jQuery
-------------------------------------
This example shows how to configure a Websocket for bidirectional communication.

.. note:: A client wishing to trigger events on the server side, shall use XMLHttpRequests (Ajax),
          as they are much more suitable, rather than messages sent via Websockets. The main purpose
          for Websockets is to communicate asynchronously from the server to the client.

Check the 'form.html' file.

Server side
-----------

The Django loop is triggered by client HTTP requests. Intentionally, there is no way to trigger events in the
Django loop through a Websocket request. Hence, all of the communication between the Websocket loop
and the Django loop must pass through the message queue.

In Webscket loop -- RedisSubscriber //not used here but  which can be modified accordingly using the 							configuration directive ``WS4REDIS_SUBSCRIBER``.

In Django loop ---- RedisPublisher

Subscribe to User Notification -- check 'views.py' file
IN the code, the message is send to the currently logged in user,  using the magic item ``SELF``.


Sending and receiving heartbeat messages
========================================

The Websocket protocol implements so called PING/PONG messages to keep Websockets alive, even behind
proxies, firewalls and load-balancers. The server sends a PING message to the client through the
Websocket, which then replies with PONG. If the client does not reply, the server closes
the connection. 

The heartbeat message, here ``--heartbeat--`` can be any magic string which does not interfere with
your remaining logic. The best way to achieve this, is to check for that magic string inside the
receive function, just before further processing the message:

The server part
---------------
The main loop of the Websocket server is idle for a maximum of 4 seconds, even if there is nothing
to do. After that time interval has elapsed, this loop optionally sends a magic string to the
client. This can be configured using the special setting:

.. code-block:: python

	WS4REDIS_HEARTBEAT = '--heartbeat--'

The purpose of this setting is twofold. During processing, the server ignores incoming messages
containing this magic string. Additionally the Websocket server sends a message with that magic
string to the client, about every four seconds. The above client code awaits these messages, at
least every five seconds, and if too many were not received, it closes the connection and tries
to reestablish it.

By default the setting ``WS4REDIS_HEARTBEAT`` is ``None``, which means that heartbeat messages are
neither expected nor sent.

As we are working on localhost , it is very less probable that connection wil close between the server and client. So I have not bothered to touch the 'heartbeat' for the sample app


Yo..Done..!!
