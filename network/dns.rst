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


    name = 'python.astrotech.io'

    answer = dns.resolver.query(name, 'MX')
    print(answer.rrset)

.. code-block:: python

    import dns.resolver

    name = 'python.astrotech.io'
    answer = dns.resolver.query(name, 'MX')

    print(answer.canonical_name)
    # readthedocs.io.

    print(answer.expiration)
    # 1541631181.7326112

    print(answer.response.answer)
    # [<DNS python.astrotech.io. IN CNAME RRset>, <DNS readthedocs.io. IN MX RRset>]

    print(answer.rrset)
    # readthedocs.io. 71 IN MX 10 aspmx3.googlemail.com.
    # readthedocs.io. 71 IN MX 10 aspmx2.googlemail.com.
    # readthedocs.io. 71 IN MX 5 alt1.aspmx.l.google.com.
    # readthedocs.io. 71 IN MX 1 aspmx.l.google.com.
    # readthedocs.io. 71 IN MX 5 alt2.aspmx.l.google.com.

    print(answer.rrset.items)
    # [
    #   <DNS IN MX rdata: 10 aspmx3.googlemail.com.>,
    #   <DNS IN MX rdata: 10 aspmx2.googlemail.com.>,
    #   <DNS IN MX rdata: 5 alt1.aspmx.l.google.com.>,
    #   <DNS IN MX rdata: 1 aspmx.l.google.com.>,
    #   <DNS IN MX rdata: 5 alt2.aspmx.l.google.com.>
    # ]



.. code-block:: python

    import dns.resolver


    name = 'python.astrotech.io'
    records = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']


    for record in records:
        answer = dns.resolver.query(name, record, raise_on_no_answer=False)

        if answer.rrset is not None:
            print(answer.rrset)


Zone transfer
-------------
* DNS Zone transfer is the process where a DNS server passes a copy of part of it's database (which is called a "zone") to another DNS server.
* DNS zone transfer, also sometimes known by the inducing DNS query type AXFR, is a type of DNS transaction.
* It is one of the many mechanisms available for administrators to replicate DNS databases across a set of DNS servers.

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
