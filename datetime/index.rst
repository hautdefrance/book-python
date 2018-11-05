**************
Dates and Time
**************

.. warning:: If you're thinking about implementing your own time calculator or system, watch Computerophile Time & Time Zones https://www.youtube.com/watch?v=-5wpm-gesOY


Date and time formats
=====================
* https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

Date formats
------------
* Which format is a formal standard in USA?
* Which format is a formal standard in Germany?
* Which format is a formal standard in Poland?

.. code-block:: text

    12.4.1961
    12.04.1961
    12 IV 1961
    12.IV.1961
    12/4/1961
    12/04/1961
    12 kwietnia 1961
    12 kwiecień 1961
    4/12/61
    April 12, 1961

Time formats
------------
* Which time is a midnight?
* Which time is a noon?

.. code-block:: text

    12:00 am
    12:00 pm
    12:00
    23:59
    24:00
    0:00
    00:00

ISO 8601 Standard
-----------------
* Dates:

    .. code-block:: text

       1961-04-12

* Date and time

.. code-block:: text

    1961-04-12T06:07:00

* Date and time with microseconds

    .. code-block:: text

        1961-04-12T06:07:00.123456


``datetime``
============

Creating ``date`` and ``datetime`` objects
------------------------------------------
.. literalinclude:: src/datetime-new.py
    :language: python
    :caption: Creating ``date`` and ``datetime`` objects

Date formatting
----------------
.. literalinclude:: src/datetime-format.py
    :language: python
    :caption: Datetime formatting as string

Parsing dates
-------------
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.

.. literalinclude:: src/datetime-parse.py
    :language: python
    :caption: Datetime parsing from string

Table of date and time parsing and formatting parameters
--------------------------------------------------------
.. note:: Prawie wszystkie parametry są podobne różnych językach programowania. Od czasu do czasu występują małe zmiany, np. w JavaScript minuty to ``i`` a nie ``M``

.. csv-table:: Tabelka parametrów formatowania i parsowania dat i czasu
    :header-rows: 1
    :file: data/datetime-formatting.csv

Time shifts and time deltas
---------------------------
.. literalinclude:: src/datetime-shift.py
    :language: python
    :caption: Shifting datetimes

.. literalinclude:: src/datetime-timedelta.py
    :language: python
    :caption: Substract time from datetimes

.. literalinclude:: src/datetime-diff.py
    :language: python
    :caption: Diff between datetimes

Time zones in ``datetime`` library
----------------------------------
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


``calendar``
============
.. literalinclude:: src/calendar-html.py
    :language: python
    :caption: HTML Calendar


``time``
========
.. literalinclude:: src/time-sleep.py
    :language: python
    :caption: Time sleep function

.. literalinclude:: src/time-timestamp.py
    :language: python
    :caption: Get timestamp


.. _timeit:

``timeit``
==========

``timeit`` from Python script
-----------------------------
.. literalinclude:: src/timeit_simple.py
    :language: python
    :caption: Timeit simple statement

.. literalinclude:: src/timeit_multiple.py
    :language: python
    :caption: Timeit multiple statements with setup code

.. literalinclude:: src/timeit_globals.py
    :language: python
    :caption: Timeit with ``globals()``

``timeit`` from terminal
------------------------
.. literalinclude:: src/timeit.sh
    :language: console
    :caption: Timeit

.. code-block:: text

    -n N, --number=N
    how many times to execute ‘statement’

    -r N, --repeat=N
    how many times to repeat the timer (default 5)

    -s S, --setup=S
    statement to be executed once initially (default pass)

    -p, --process
    measure process time, not wallclock time, using time.process_time() instead of time.perf_counter(), which is the default

    -u, --unit=U
    specify a time unit for timer output; can select nsec, usec, msec, or sec

    -v, --verbose
    print raw timing results; repeat for more digits precision

    -h, --help
    print a short usage message and exit


Assignments
===========

Date manipulation
------------------
#. Dane są dwie następujące daty w formacie jak poniżej:

    .. code-block:: python

        date1 = 'April 12, 1961 2:07 local time'  # Asia/Almaty
        date2 = '"07/21/69 2:56:15 AM UTC"'

#. Przedstaw daty jako obiekt ``datetime``
#. Wyświetl daty w formacie ISO, e.g. "1961-04-12T06:07:00.123456" w UTC
#. Odejmij obie daty od siebie
#. Oblicz ile lat i miesięcy minęło między wydarzeniami
#. Od obecnej chwili (UTC) odejmij ten sam czas, który Ci wyszedł w poprzednim punkcie
#. Wyświetl samą datę (bez czasu)
#. Ile miałeś wtedy lat?
#. Przyjmij:

    - rok = 365.2425 dni
    - miesiac = 30.436875 dni

:About:
    * Filename: ``datetime_deltas.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 20 min

:Zadanie z gwiazdką:
    * Co to za daty, które podał użytkownik?
    * Uwzględnij strefy czasowe.
    * Co robiłeś przez ten czas?

:Hint:
    * Wpisz "local time" jako zwykły tekst do ``strptime``
    * Standard ISO:

        * '1961-04-12'
        * '1961-04-12T06:07:00'
        * '1961-04-12T06:07:00.123456'
