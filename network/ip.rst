*********
IPv4/IPv6
*********


* https://yamakira.github.io/python-network-programming/libraries/netaddr/index.html

``netaddr``
===========

Installation
------------
.. code-block:: console

    pip install netaddr

Layer 3 addressing (IP)
-----------------------
.. code-block:: python

    from netaddr import IPAddress

    ip = IPAddress('192.21.8.11')

    ip.version
    # 4

    dir(ip)
    # [ ... Snipped... 'bin', 'bits', 'format', 'info', 'ipv4', 'ipv6',
    # 'is_hostmask', 'is_ipv4_compat', 'is_ipv4_mapped', 'is_link_local',
    # 'is_loopback', 'is_multicast', 'is_netmask', 'is_private', 'is_reserved',
    # 'is_unicast', 'key', 'netmask_bits', 'packed', 'reverse_dns', 'sort_key',
    # 'value', 'version', 'words']

.. code-block:: python

    ip.bin
    # '0b11000000000101010000100000001011'

    ip.bits()
    # '11000000.00010101.00001000.00001011'

    ip.words
    # (192, 21, 8, 11)

    ip.packed
    # '\xc0\x15\x08\x0b'

.. code-block:: python

    ip.version
    # 6

    ip.is_unicast()
    # True

    ip.is_link_local()
    # True

IPNetwork
---------
.. code-block:: python

    from netaddr import IPNetwork

    ip_range = IPNetwork('192.241.21.6/24')

    dir(ip_range)
    # [ ... snipped ...  'broadcast', 'cidr', 'first', 'hostmask', 'info',
    # 'ip', 'ipv4', 'ipv6', 'is_ipv4_compat', 'is_ipv4_mapped', 'is_link_local',
    # 'is_loopback', 'is_multicast', 'is_private', 'is_reserved', 'is_unicast',
    # 'iter_hosts', 'key', 'last', 'netmask', 'network', 'next', 'prefixlen',
    # 'previous', 'size', 'sort_key', 'subnet', 'supernet', 'value', 'version']

.. code-block:: python

    ip_range.network
    # IPAddress('192.241.21.0')

    ip_range.hostmask
    # IPAddress('0.0.0.255')

    ip_range.netmask
    # IPAddress('255.255.255.0')

    ip_range.broadcast
    # IPAddress('192.241.21.255')

    ip_range.size
    # 256

.. code-block:: python

    for i in ip_range:
         print(i)

    # 192.241.21.0
    # 192.241.21.1
    # ... snipped ...
    # 192.241.21.255

List operations on IPNetwork object
-----------------------------------
.. code-block:: python

    ip_range = IPNetwork('192.0.2.16/29')
    
    ip_range_list = list(ip_range)
    
    len(ip_range_list)
    # 8

    ip_range_list
    # [IPAddress('192.0.2.16'), IPAddress('192.0.2.17'), ...snipped... IPAddress('192.0.2.23')]
    
    ip_range_list[6]        # indexing
    # IPAddress('192.0.2.22')
    
    ip_range_list[2:5]      # slicing
    # [IPAddress('192.0.2.18'), IPAddress('192.0.2.19'), IPAddress('192.0.2.20')]

IPRange
-------
.. code-block:: python

    ip_range = IPRange('192.168.1.0', '192.168.1.20')
    
    for i in ip_range:
         print(i)

    # 192.168.1.0
    # ... snipped ...
    # 192.168.1.19
    # 192.168.1.20

IP sets
-------
.. code-block:: python

    IPSet(['192.0.2.0'])
    # IPSet(['192.0.2.0/32'])
    
    IPSet([IPAddress('192.0.2.0')])
    # IPSet(['192.0.2.0/32'])
    
    IPSet([IPNetwork('192.0.2.0/24')])
    # IPSet(['192.0.2.0/24'])
    
    IPSet(IPRange("10.0.0.0", "10.0.1.31"))
    # IPSet(['10.0.0.0/24', '10.0.1.0/27'])

.. code-block:: python

    for ip in IPSet(['192.0.2.0/28']):
         print(ip)

    # 192.0.2.0
    # 192.0.2.1
    # ... snipped ...
    # 192.168.2.15

Adding and removing set elements
--------------------------------
.. code-block:: python

    from netaddr import IPSet
    
    s1 = IPSet()

    s1.add('192.168.1.0/30')
    s1.size
    # 4
    
    '192.168.1.3' in s1
    # True
    
    s1.remove('192.168.1.3')
    s1.size
    # 3

.. code-block:: python

    scan1 = IPSet(['192.168.1.0/30'])
    
    scan1
    # IPSet(['192.168.1.0/30'])
    
    scan1.size
    # 4
    
    scan2 = IPSet(['192.168.1.0/31'])
    
    scan2.size
    # 2
    
    scan1 | scan2
    # IPSet(['192.168.1.0/30'])
    
    scan1 & scan2
    # IPSet(['192.168.1.0/31'])
    
    scan1 ^ scan2
    # IPSet(['192.168.1.2/31'])

Layer 2 addressing (MAC)
------------------------
.. code-block:: python

    mac = EUI('ec:f4:bb:87:2d:0c')

    dir(mac)
    # ... snipped ... 'bin', 'bits', 'dialect', 'ei', 'eui64', 'iab',
    # 'info', 'ipv6', 'ipv6_link_local', 'is_iab', 'modified_eui64', 'oui',
    # 'packed', 'value', 'version', 'words']

    str(mac), str(mac.ei), str(mac.oui), str(mac.version)
    # ('EC-F4-BB-87-2D-0C', '87-2D-0C', 'EC-F4-BB', '48')

.. code-block:: python

    mac.info
    # {'OUI': {'address': ['one dell way',
    #              'MS:RR5-45',
    #              'Round rock Texas 78682',
    #              'UNITED STATES'],
    #  'idx': 15529147,
    #  'offset': 3429092,
    #  'org': 'Dell Inc',
    #  'oui': 'EC-F4-BB',
    #  'size': 141}}

.. code-block:: python

    oui = mac.oui
    
    dir(oui)
    # [ ... snipped ... 'records', 'reg_count', 'registration']
    
    oui.registration().org
    # 'Dell Inc'
    
    oui.registration().address
    # ['one dell way', 'MS:RR5-45', 'Round rock Texas 78682', 'UNITED STATES']
