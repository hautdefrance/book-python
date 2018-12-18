**********
While loop
**********


Declaration
===========
* Continue execution when argument is ``True``

Never ending loop
-----------------
.. code-block:: python

    while True:
        pass

Stop conditions
---------------
.. code-block:: python

    i = 0

    while i <= 5:
        print(i)
        i += 1

    # 0
    # 1
    # 2
    # 3
    # 4
    # 5

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
#. Za pomocą pętli przekonwertuj skalę na ``List[float]``
#. Użytkownik podaje oceny jako ``int`` lub ``float`` (nie będzie próbował psuć)
#. Jeżeli ocena jest na liście dopuszczalnych ocen, dodaj ją do dzienniczka
#. Jeżeli wciśnięto sam Enter, zakończ wpisywanie do dzienniczka
#. Jeżeli wpisano cyfrę nie znajdującą się na liście dopuszczalnych ocen, wyświetl informację "Grade is not allowed" i dalej kontynuuj wpisywanie
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
