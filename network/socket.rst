******
Socket
******


``socket``
==========
.. figure:: img/socket-flow.jpg
    :scale: 50%
    :align: center

    Socket Flow

Protocols
---------
* IPv4 - ``socket.AF_INET``
* IPv6 - ``socket.AF_INET6``
* UDP - ``socket.SOCK_DGRAM``
* TCP - ``socket.SOCK_STREAM``
* Broadcast - ``socket.SO_BROADCAST``

API
---
* The ``bufsize`` argument of 1024 used above is the maximum amount of data to be received at once
* ``accept()``, ``connect()``, ``send()``, and ``recv()`` are blocking
* Blocking calls have to wait on system calls (I/O) to complete before they can return a value

.. csv-table:: API
    :header-rows: 1

    "Method", "Description"
    "``socket()``", ""
    "``bind()``", ""
    "``listen()``", ""
    "``accept()``", ""
    "``connect()``", ""
    "``connect_ex()``", ""
    "``send()``", ""
    "``recv()``", ""
    "``close()``", ""

TCP
---

Server
^^^^^^
.. literalinclude:: src/socket-tcp-server.py
    :language: python
    :caption: ``socket`` TCP Server

Client
^^^^^^
.. literalinclude:: src/socket-tcp-client.py
    :language: python
    :caption: ``socket`` TCP Client

UDP
---

Server
^^^^^^
.. literalinclude:: src/socket-udp-server.py
    :language: python
    :caption: ``socket`` UDP Server

Client
^^^^^^
.. literalinclude:: src/socket-udp-client.py
    :language: python
    :caption: ``socket`` UDP Client

Multicast
---------
.. literalinclude:: src/socket-multicast.py
    :language: python
    :caption: ``socket`` Multicast Client


``socketserver``
================

TCP
---

Server
^^^^^^
.. literalinclude:: src/socketserver-tcp-server.py
    :language: python
    :caption: ``socketserver`` TCP Server

Client
^^^^^^
.. literalinclude:: src/socket-tcp-client.py
    :language: python
    :caption: ``socket`` TCP Client

Asynchronous
------------
.. code-block:: python


References
==========
* https://realpython.com/python-sockets/
