.. _Loops:

********
For loop
********


Iterating over ``str``
======================
* Iterating ``str`` will get character on each iteration:

    .. code-block:: python

        for character in 'setosa':
            print(character)

        # s
        # e
        # t
        # o
        # s
        # a


Iterating simple collections
============================

Iterating over ``list``
-----------------------
.. code-block:: python

    DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']

    for element in DATA:
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Iterating over ``tuple``
------------------------
.. code-block:: python

    DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for element in DATA:
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Iterating over ``set``
----------------------
.. code-block:: python

    DATA = {5.1, 3.5, 1.4, 0.2, 'setosa'}

    for element in DATA:
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Loops with ``range``
--------------------
* ``range(0, 5)`` will generate ``(0, 1, 2, 3, 4)``

.. code-block:: python

    for number in range(0, 5):
        print(number)

    # 0
    # 1
    # 2
    # 3
    # 4


Assignments
===========

Counter
-------
#. Dane są liczby:

.. code-block:: python

    [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
     0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
     2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
     1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
     4, 8, 1, 9, 6, 3]

#. Policz ile jest wystąpień każdej z cyfr w tej liście
#. Zwróć ``counter: Dict[int, int]``

    - klucz - cyfra
    - wartość - ilość wystąpień

:About:
    * Filename: ``loop_dict_counter.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Iterowanie po liście

Text manipulation
-----------------
#. Dany jest tekst przemównienia John F. Kennedy'ego "Moon Speech" wygłoszony na Rice Stadium

    .. code-block:: text

        We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win

#. Zdania oddzielone są kropkami
#. Każde zdanie oczyść z białych znaków na początku i końcu
#. Wyrazy oddzielone są spacjami
#. Policz ile jest wyrazów w każdym zdaniu
#. Wypisz na ekranie słownik o strukturze:

    * ``Dict[str, int]``
    * klucz: zdanie
    * wartość: ilość wyrazów

#. Na końcu wypisz także ile jest:

    * zdań
    * słów
    * znaków (łącznie ze spacjami wewnątrz zdań, ale bez kropek)

:About:
    * Filename: ``loop_sentences.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 10 min

:Co zadanie sprawdza:
    * Dzielenie stringów
    * Sprawdzanie długości ciągów znaków
    * Iterowanie po elementach listy
    * Nazywanie zmiennych

:Hint:
    * ``zdania = TEXT.split('.')``
