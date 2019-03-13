**************
``while`` loop
**************


Syntax
======
* Continue execution when argument is ``True``

Generic syntax
--------------
.. code-block:: python
    :caption: ``while`` loop generic syntax

    while CONDITION:
        ...

Example
=======

Never ending loop
-----------------
.. code-block:: python

    while True:
        print('hello')

Stop conditions
---------------
.. code-block:: python

    i = 0

    while i <= 3:
        print(i)
        i += 1

    # 0
    # 1
    # 2

.. code-block:: python

    i = 0
    numbers = [1, 2, 3]

    while i <= len(numbers):
        current = numbers[i]
        print(current)
        i += 1

    # 1
    # 2
    # 3

Exit flag
---------
.. code-block:: python

    i = 0
    exit_flag = False

    while not exit_flag:
        if i % 2 == 0:
            exit_flag = True

        print(i)
        i += 1

    # 0

``else``
--------


``break`` and ``continue``
==========================

Skipping iterations
-------------------
.. code-block:: python

    i = 0

    while i <= 10:
        i += 1

        if i % 2 == 0:
            continue

        print(i)

    # 1
    # 3
    # 5


Exiting the loop
----------------
.. code-block:: python

    while True:
        number = input('Type number: ')

        # if user hit enter, without typing number
        if not number:
            break


Assignments
===========

Report card
-----------
* Filename: ``loop_report_card.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Do zmiennej zapisz skalę ocen ``(2, 3, 3.5, 4, 4.5, 5)``
#. Za pomocą pętli ``while`` przekonwertuj skalę na zmienną typu ``List[float]``
#. Użytkownik podaje oceny jako ``int`` lub ``float``, nie będzie próbował podawać niepoprawnych typów, np. ``str`` albo ``float`` z przecinkiem zamiast kropki
#. Jeżeli wciśnięto sam Enter, zakończ wpisywanie do dzienniczka
#. Jeżeli ocena na liście dopuszczalnych ocen:

    - Jest: dodaj ją do dzienniczka
    - Nie ma: wyświetl informację "Grade is not allowed" i dalej kontynuuj wpisywanie

#. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną z ocen

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Generowanie struktur danych i konwersja typów
    * Weryfikacja ciągu wprowadzonego od użytkownika
    * Korzystanie z pętli oraz instrukcji wychodzących
    * Konwersja typów i rzutowanie
    * Sprawdzanie czy obiekt jest instancją klasy
    * Wykorzystanie funkcji wbudowanych

:Hints:
    * ``average = sum(...) / len(...)``
