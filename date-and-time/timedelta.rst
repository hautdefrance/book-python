***********
Time Deltas
***********


Time shifts
===========
.. literalinclude:: src/timedelta-shift.py
    :language: python
    :caption: Shifting datetime objects


``timedelta``
=============

Simple ``timedelta`` shifts
---------------------------
.. literalinclude:: src/timedelta-simple.py
    :language: python
    :caption: Simple ``timedelta`` shifts

Complex ``timedelta`` shifts
----------------------------
.. literalinclude:: src/timedelta-complex.py
    :language: python
    :caption: Complex ``timedelta`` shifts

``timedelta`` month shifts
--------------------------
.. literalinclude:: src/timedelta-month.py
    :language: python
    :caption: Subtract month from ``datetime``


Time diff
=========
.. literalinclude:: src/timedelta-diff.py
    :language: python
    :caption: Diff between datetime objects


Assignments
===========

Date manipulation
------------------
* Filename: ``datetime_deltas.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

#. Dane są dwie następujące daty w formacie jak poniżej:

    .. code-block:: python

        gagarin = 'April 12, 1961 2:07 local time'  # Asia/Almaty
        armstrong = '"07/21/69 2:56:15 AM UTC"'

#. Przedstaw daty jako obiekt ``datetime``
#. Odejmij obie daty od siebie
#. Oblicz ile lat i miesięcy minęło między wydarzeniami
#. Od obecnej chwili odejmij ten sam czas, który Ci wyszedł w poprzednim punkcie
#. Wyświetl samą datę (bez czasu)
#. Ile miałeś wtedy lat?
#. Przyjmij:

    - rok = 365.2425 dni
    - miesiąc = 30.436875 dni

:Zadanie z gwiazdką:
    * Co robiłeś przez ten czas?

:Hint:
    * Wpisz "local time" jako zwykły tekst do ``strptime``
    * ``datetime.now(tz=timezone.utc)``
    * ``datetime(1961, 04, 12, 6, 7).replace(tz=timezone.utc)``
    * Standard ISO:

        * '1961-04-12'
        * '1961-04-12T06:07:00'
        * '1961-04-12T06:07:00.123456'
