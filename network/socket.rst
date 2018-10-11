*******************
Network Programming
*******************

Socket
======

Protokoły
---------
* IPv4 - ``socket.AF_INET``
* IPv6 - ``socket.AF_INET6``
* UDP - ``socket.SOCK_DGRAM``
* TCP - ``socket.SOCK_STREAM``

Otwieranie połączeń
-------------------
.. literalinclude:: src/socket-communication.py
    :name: listing-socket-communication
    :language: python
    :caption: Komunikacja za pomocą socketów

Nasłuchiwanie
-------------
.. code-block:: python

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(bytes('%s:%s\n', 'utf-8'), addr)

Przekazywanie informacji
------------------------

Biblioteki sieciowe
===================

``smtp``
--------

Zastosowania sieciowe
---------------------
* Scapy http://www.secdev.org/projects/scapy/

Automatyzacja pracy
===================

``fabric``
----------
* http://www.fabfile.org/
* https://pypi.python.org/pypi/Fabric3

.. code-block:: python

    from fabric.api import hosts

    @hosts(['127.0.0.1', 'localhost'])
    def whoami():
        sudo('whoami')


Allegro Ralph
=============
* http://allegro.tech/ralph/
* https://github.com/allegro/ralph

Ralph is full-featured Asset Management, DCIM and CMDB system for data center and back office.

Features:

- keep track of assets purchases and their life cycle
- generate flexible and accurate cost reports
- integrate with change management process using JIRA integration

It is an Open Source project provided on Apache v2.0 License.

Live demo:

- http://ralph-demo.allegro.tech/
- login: ralph
- password: ralph

``ldap3``
=========
:numref:`listing-opensource-ldap-expiring-passwords`
