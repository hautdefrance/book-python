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

    4/12/61
    April 12, 1961

    12.4.1961
    12.04.1961

    12 IV 1961
    12.IV.1961

    12/4/1961
    12/04/1961

    12 kwietnia 1961
    12 kwiecień 1961

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


Creating ``date`` objects
=========================

Create ``date``
---------------
.. literalinclude:: src/date-new.py
    :language: python
    :caption: Creating ``date`` objects

Current ``date``
----------------
.. literalinclude:: src/date-today.py
    :language: python
    :caption: Creating ``date`` objects


Creating ``datetime`` objects
=============================

Create ``datetime``
-------------------
.. literalinclude:: src/datetime-new.py
    :language: python
    :caption: Creating ``datetime`` objects

Current ``datetime``
--------------------
.. literalinclude:: src/datetime-now.py
    :language: python
    :caption: Creating ``datetime`` objects


Parsing and formatting dates and time
=====================================

Table of date and time parsing and formatting parameters
--------------------------------------------------------
.. note:: Prawie wszystkie parametry są podobne różnych językach programowania. Od czasu do czasu występują małe zmiany, np. w JavaScript minuty to ``i`` a nie ``M``

.. csv-table:: Tabelka parametrów formatowania i parsowania dat i czasu
    :header-rows: 1
    :file: data/datetime-formatting.csv

``f-string formatting``
-----------------------
.. literalinclude:: src/datetime-format.py
    :language: python
    :caption: Datetime formatting as string with ``f'...'``

Format to string
----------------
.. literalinclude:: src/datetime-strftime.py
    :language: python
    :caption: Datetime formatting as string with ``.strftime()``

Parsing dates
-------------
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.

.. literalinclude:: src/datetime-parse.py
    :language: python
    :caption: Datetime parsing from string


Assignments
===========

From ISO date format
--------------------
#. Dane są dwie następujące daty w formacie jak poniżej:

    .. code-block:: python

        gagarin = '1961-04-12T06:07:00.123456'
        armstrong = '1969-07-21T14:56:15.123456'

#. Przedstaw daty jako obiekt ``datetime``
#. Wyświetl pierwszą datę w formacie Amerykańkim "Miesiąc Dzień, Rok Godzina:Minuta AM/PM"
#. Wyświetl drugą datę w formacie Niemieckim "Dzień.Miesiąc.Rok"

:About:
    * Filename: ``datetime_from_iso.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

To ISO date format
------------------
#. Dane są dwie następujące daty w formacie jak poniżej:

    .. code-block:: python

        date1 = 'April 12, 1961 2:07 local time'
        date2 = '"07/21/69 2:56:15 AM UTC"'

#. Przedstaw daty jako obiekt ``datetime``
#. Wyświetl ``date1`` w formacie ISO, tj. "Rok-Miesiąc-DzieńTGodzina:Minuta:Sekunda.UłamkiSekund"
#. Wyświetl ``date2`` samą datę, tj. bez czasu

:About:
    * Filename: ``datetime_to_iso.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 15 min

:Hint:
    * Wpisz "local time" jako zwykły tekst do ``strptime``
    * Znaki znaki cudzysłowia jako znaczki do ``strptime``
