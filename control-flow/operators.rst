.. _Operators:

*********
Operators
*********


Operator precedence
===================
.. csv-table:: Operator precedence
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-precedence.csv


Assignments
===========

Even and odd numbers
--------------------
#. Wczytaj od użytkownika ciąg znaków dowolnej długości
#. Użytkownik poda wyłącznie ciągi znaków parsujące się do ``int`` lub ``float`` bez błędów
#. Sprawdź czy jest to liczba parzysta, czy nieparzysta

:About:
    * Filename: ``operators_even_odd.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie
    * wykorzystanie operatorów matematycznych

:Hints:
    * Zero jest parzyste: https://en.wikipedia.org/wiki/Parity_of_zero
    * Liczba parzysta, to taka, która po podzieleniu przez dwa nie ma reszty
    * Zwróć uwagę, że operator ``%`` działa modulo tylko na ``int`` oraz na ``float``. Przy ``str`` ma zupełnie inne znaczenie.
