**********
Interfaces
**********


``netifaces``
=============

Installation
------------
.. code-block:: console

    pip install netifaces

Basic operations
----------------
.. code-block:: python

    import netifaces

    dir(netifaces)
    # [ ... snipped ...
    # 'address_families', 'gateways', 'ifaddresses', 'interfaces', 'version']

List network interfaces
-----------------------
.. code-block:: python

    import netifaces

    netifaces.interfaces()
    # ['lo', 'eth0', 'wlan0', 'eth3', 'vboxnet0']

Addresses of a interface
------------------------
.. code-block:: python

    import netifaces
    from pprint import pprint


    pprint(netifaces.ifaddresses('eth3'))
    # {2: [{'addr': '192.168.1.100',
    #       'broadcast': '192.168.1.255',
    #       'netmask': '255.255.255.0'}],
    #  10: [{'addr': 'fe80::364b:50ff:feb7:ef1d%eth3',
    #        'netmask': 'ffff:ffff:ffff:ffff::/64'}],
    #  17: [{'addr': '34:4b:50:b7:ef:1d', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]}

List Gateways
-------------
.. code-block:: python

    import netifaces

    netifaces.gateways()
    # {'default': {2: ('192.168.1.1', 'eth3')}, 2: [('192.168.1.1', 'eth3', True)]}

Getting list of IPv4 addresses excluding loopback and virtualbox adapters
-------------------------------------------------------------------------
.. code-block:: python

    for iface in netifaces.interfaces():
         if iface == 'lo' or iface.startswith('vbox'):
             continue

         iface_details = netifaces.ifaddresses(iface)

         if iface_details.has_key(netifaces.AF_INET):
             print iface_details[netifaces.AF_INET]

    # [{'broadcast': '192.168.1.255', 'netmask': '255.255.255.0', 'addr': '192.168.1.100'}]
    # [{'broadcast': '192.168.1.255', 'netmask': '255.255.255.0', 'addr': '192.168.1.101'}]

.. note:: More examples: https://www.programcreek.com/python/example/81895/netifaces.interfaces
