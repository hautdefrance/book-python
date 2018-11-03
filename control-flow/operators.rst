.. _Operators:

*********
Operators
*********


General operators
=================
.. csv-table:: Universal operators
    :header-rows: 1
    :widths: 15, 25, 60
    :file: data/operators-general.csv


Numerical types operators
=========================
.. csv-table:: Numerical types operators
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-numerical.csv


Bitwise operators
=================
- ``|`` - OR
- ``&`` - AND
- ``~`` - NOT
- ``^`` - XOR
- ``<<`` - Shift left
- ``>>`` - Shift right

.. code-block:: python

    0 ^ 0  # 0
    1 ^ 1  # 0
    1 ^ 0  # 1
    0 ^ 1  # 1
    8 ^ 5  # 13

.. code-block:: text

    1000  # 8 (binary)
    0101  # 3 (binary)
    ----  # APPLY XOR ('vertically')
    1101  # result = 13 (dec)


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

Integers and floats
-------------------
#. Wczytaj liczbę od użytkownika (poda tylko ``int`` albo ``float``)
#. Wyświetl informację czy jest to liczba całkowita, czy niecałkowita.

:About:
    * Filename: ``operators_integers.py``
    * Lines of code to write: 7 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie

:Hints:
    * Liczba całkowita to taka, której część dziesiętna nie występuje lub jest równa zero.
    * Możesz to sprawdzić dzieląc liczbę z resztą przez *1* i sprawdzając resztę z dzielenia.
    * Zwróć uywagę, że ``input()`` zawsze zwraca ``str`` wiec trzeba rzutowac na ``int``, ale wtedy tracimy informację czy wczesniej mielismy ``float``
