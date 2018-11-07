****
IMAP
****


Connection
==========
* ``imaplib.IMAP4(host, port)``, If port is omitted, the standard IMAP4 port (143) is used.
* ``imaplib.IMAP4_SSL(host, port)``, if port is omitted, the standard IMAP4-over-SSL port (993)


Methods
=======
.. csv-table:: python
    :header-rows: 1
    :file: data/imap-api.csv


Usage
=====
.. literalinclude:: src/imap-usage.py
    :language: python
    :caption: Usage


Case Study for Gmail IMAP
=========================
.. literalinclude:: src/imap-gmail.py
    :language: python
    :caption: Case Study for Gmail IMAP
