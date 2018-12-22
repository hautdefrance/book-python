**********************
Parsing and Formatting
**********************


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

.. code-block:: text

    12.4.1961
    12.04.1961

.. code-block:: text

    12 IV 1961
    12.IV.1961

.. code-block:: text

    12/4/1961
    12/04/1961

.. code-block:: text

    12 kwietnia 1961
    12 kwiecień 1961

Time formats
------------
* Which time is a midnight?
* Which time is a noon?

.. code-block:: text

    12:00 am
    12:00 pm

* Are those times correct?

.. code-block:: text

    12:00
    23:59
    24:00
    0:00
    00:00

ISO 8601 Standard
-----------------
* "Z" (Zulu) means UTC

* Dates:

    .. code-block:: text

       1961-04-12

* Date and time

    .. code-block:: text

        1961-04-12T06:07:00Z

* Date and time with miliseconds

    .. code-block:: text

        1961-04-12T06:07:00.123Z

* Date and time with microseconds

    .. code-block:: text

        1961-04-12T06:07:00.123456Z


Table of date and time parsing and formatting parameters
========================================================
.. note:: Prawie wszystkie parametry są podobne różnych językach programowania. Od czasu do czasu występują małe zmiany, np. w JavaScript minuty to ``i`` a nie ``M``

.. csv-table:: Tabelka parametrów formatowania i parsowania dat i czasu
    :header-rows: 1
    :file: data/datetime-formatting.csv


``f-string`` formatting
=======================
.. literalinclude:: src/datetime-format.py
    :language: python
    :caption: Datetime formatting as string with ``f'...'``


Format to string
================
.. literalinclude:: src/datetime-strftime.py
    :language: python
    :caption: Datetime formatting as string with ``.strftime()``


Parsing dates
=============
* Parsing - analyze (a sentence) into its parts and describe their syntactic roles.

.. literalinclude:: src/datetime-parse.py
    :language: python
    :caption: Datetime parsing from string


Assignments
===========

From ISO date format
--------------------
* Filename: ``datetime_from_iso.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Input data: :numref:`listing-time-from-iso`

#. Przedstaw datę jako obiekt ``datetime``

.. code-block:: text
    :name: listing-time-from-iso
    :caption: Convert ``str`` from ISO date format to ``datetime`` objects

    1969-07-21T14:56:15.123Z

To ISO date format
------------------
* Filename: ``datetime_to_iso.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Datę:

    .. code-block:: python

        datetime.datetime(1961, 4, 12, 6, 7, 0, 123456)

#. Przedstaw daty jako obiekt ``datetime``
#. Wyświetl w formacie ISO datę i czas, tj.:

    .. code-block:: text

        "Rok-Miesiąc-DzieńTGodzina:Minuta:Sekunda.UłamkiSekundZ"
        1961-04-12T06:07:00.123456Z

#. Wyświetl w formacie ISO samą datę, tj. bez czasu:

    .. code-block:: text

        "Rok-Miesiąc-Dzień"
        1961-04-12

US date and time format
-----------------------
* Filename: ``datetime_from_us.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Rozczytaj datę z formatu Amerykańkiego długiego:

    .. code-block:: text

        "April 12, 1961 06:07:00 AM local time"

#. Wyświetl datę w formacie Amerykańkim krótkim:

    .. code-block:: text

        "Miesiąc/Dzień/Rok Godzina:Minuta AM/PM"
        04/12/61 06:07 AM

:Hint:
    * Wpisz "local time" jako część stringa (formatu) do``strptime``
    * Wpisz znaki cudzysłowia jako część stringa (formatu) do ``strptime``
