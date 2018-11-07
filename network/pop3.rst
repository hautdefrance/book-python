****
POP3
****


Connection
==========
* If port is not specified, the standard POP3 port (110)
* If port is not specified, 995, the standard POP3-over-SSL port is used


``poplib`` API
==============
.. csv-table:: ``poplib`` API
    :header-rows: 1
    :file: data/pop3-api.csv


Retrieve Messages with POP3
===========================
.. literalinclude:: src/pop3-retrieve.py
    :language: python
    :caption: Secured connection to the SMTP server
