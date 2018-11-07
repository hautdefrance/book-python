************
DNS Protocol
************

* https://yamakira.github.io/python-network-programming/protocols/dns/index.html


``dnspython``
=============

Installation
------------
.. code-block:: console

    $ pip install dnspython

Basic DNS queries
-----------------
.. code-block:: python

    import dns.resolver


    name = 'iana.org'

    for qtype in 'A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA':
        answer = dns.resolver.query(name,qtype, raise_on_no_answer=False)

        if answer.rrset is not None:
            print(answer.rrset)

Zone transfer
-------------
.. code-block:: python

    import dns.query
    import dns.zone

    z = dns.zone.from_xfr(dns.query.xfr('nsztm1.digi.ninja', 'zonetransfer.me'))
    names = z.nodes.keys()
    names.sort()
    for n in names:
        print z[n].to_text(n)

Reverse DNS lookup (PTR record)
-------------------------------
* Reverse DNS resolution (rDNS) is the determination of a domain name associated with an IP address via querying DNS (the reverse of the usual “forward” DNS lookup of an IP from a domain name.)
* To do a reverse lookup of the IP address 8.8.4.4 the PTR record for the domain name 4.4.8.8.in-addr.arpa would be looked up, and found to point to google-public-dns-b.google.com.

.. code-block:: python

    from dns import reversename


    domain_address = reversename.from_address('8.8.4.4')

    print(domain_address)
    # 4.4.8.8.in-addr.arpa.

    ip_address = reversename.to_address(domain_address)
    print(ip_address)
    # 8.8.4.4

.. code-block:: python

    from dns import resolver

    domain_name = str(resolver.query(domain_address,"PTR")[0])
    print(domain_name)
    # google-public-dns-b.google.com.
