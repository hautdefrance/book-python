*********
Timezones
*********


Time zones in ``datetime`` library
==================================
* Always keep dates and times only in UTC (**important!**)
* Datetimes should be converted to localtime only when displaying to user

.. literalinclude:: src/datetime-tzinfo.py
    :language: python
    :caption: Make timezone aware object from naive datetime


``pytz``
========

List of Timezones
-----------------
* https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
* https://www.iana.org/time-zones

.. literalinclude:: src/pytz-tzlist.py
    :language: python
    :caption: ``pytz`` brings the Olson tz database into Python.

From naive to local
-------------------
.. literalinclude:: src/pytz-naive-to-local.py
    :language: python
    :caption: From naive to local time

From naive to UTC
-----------------
.. literalinclude:: src/pytz-naive-to-utc.py
    :language: python
    :caption: From naive to local time

From UTC to local time
----------------------
.. literalinclude:: src/pytz-utc-to-local.py
    :language: python
    :caption: From UTC to local time

Between timezones
-----------------
.. literalinclude:: src/pytz-between-timezones.py
    :language: python
    :caption: Between timezones


Assignments
===========

Time zone converting
--------------------
* Filename: ``datetime_tz.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Dane są dwie następujące daty w formacie jak poniżej:

    .. code-block:: python

        gagarin = 'April 12, 1961 2:07 local time'  # Asia/Almaty
        armstrong = '"07/21/69 2:56:15 AM UTC"'

#. Przedstaw daty jako obiekt ``datetime`` ze strefą czasową UTC
#. Wyświetl obie daty w formacie *ISO* w strefie czasowej ``Europe/Warsaw``

:Hint:
    * Wpisz "local time" jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
    * Wpisz znaki cudzysłowia ``"`` jako zwykły tekst w parametrze ``fmt`` funkcji ``.strptime()``
    * Standard ISO:

        * '1961-04-12'
        * '1961-04-12T06:07:00Z'
        * '1961-04-12T06:07:00.123456Z'
