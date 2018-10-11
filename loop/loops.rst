.. _Loops:

*****
Loops
*****


``while``
=========
* Continue execution when argument is ``True``

.. code-block:: python

    while True:
        pass

.. code-block:: python

    i = 0

    while i <= 10:
        print(x)
        i += 1


``for``
=======

Iterating over ``str``
----------------------
* Iterating ``str`` will get character on each iteration:

    .. code-block:: python

        for character in 'Hello':
            print(character)

        # H
        # e
        # l
        # l
        # o

Iterating simple collections
----------------------------
* Iterating over ``list``:

    .. code-block:: python

        DATA = [1, 2.5, 'Jose Jimenez']

        for element in DATA:
            print(element)

        # 1
        # 2.5
        # 'Jose Jimenez'

* Iterating over ``tuple``:

    .. code-block:: python

        DATA = (1, 2.5, 'Jose Jimenez')

        for element in DATA:
            print(element)

        # 1
        # 2.5
        # 'Jose Jimenez'

* ``range(0, 5)`` will generate ``(0, 1, 2, 3, 4)``

    .. code-block:: python

        for number in range(0, 5):
            print(f'Value is: {number}')

        # Value is: 0
        # Value is: 1
        # Value is: 2
        # Value is: 3
        # Value is: 4

Iterating over nested ``list`` items
------------------------------------
.. code-block:: python

    DATA = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
    ]

    for element in DATA:
        print(element)

    # ('a', 0)
    # ('b', 1)
    # ('c', 2)

.. code-block:: python

    a, b = 'a', 0
    a, b = ('a', 0)
    key, value = ('a', 0)

.. code-block:: python

    DATA = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
    ]

    for key, value in DATA:
        print(f'key: "{key}", value: "{value}"')

    # key: "a", value: "0"
    # key: "b", value: "1"
    # key: "c", value: "2"

.. code-block:: python

    DATA = [
        (0, 1),
        ('name', 'José'),
        ('locations', ['CapeCanaveral', 'Houston']),
    ]

    for key, value in DATA:
        print(f'key: "{key}", value: "{value}"')

    # key: "0",         value: "1"
    # key: "name",      value: "José"
    # key: "locations", value: "['CapeCanaveral', 'Houston']"

``enumerate()``
---------------
.. code-block:: python

    DATA = ['a', 'b', 'c']

    for element in DATA:
        print(element)
    # a
    # b
    # c

    for index, element in enumerate(DATA):
        print(index, element)
    # 0 a
    # 1 b
    # 2 c


Iterating over ``dict`` items
-----------------------------
* ``dict`` elements order changes!
* Iterating over ``dict`` values:

    .. code-block:: python

        DATA = {
            'first_name': 'José',
            'last_name': 'Jiménez',
            'age': 42,
        }

        DATA.values()
        # ['José', 'Jiménez', 42]

        for element in DATA.values():
            print(element)

        # 'José'
        # 'Jiménez'
        # 42

* Iterating over ``dict`` keys:

    .. code-block:: python

        DATA = {
            'first_name': 'José',
            'last_name': 'Jiménez',
            'age': 42,
        }

        my_dict.keys()
        # ['first_name', 'last_name', 'age']

        for element in DATA.keys():
            print(element)

        # 'first_name'
        # 'last_name'
        # 'age'

* By default ``dict`` iterates over keys:

    .. code-block:: python

        DATA = {
            'first_name': 'José',
            'last_name': 'Jiménez',
            'age': 42,
        }

        for element in DATA:
            print(element)

        # 'first_name'
        # 'last_name'
        # 'age'

* Getting pair: ``key``, ``value`` from ``dict`` items:

    .. code-block:: python

        DATA = {
            'first_name': 'José',
            'last_name': 'Jiménez',
            'age': 42,
        }

        DATA.items()
        # [('first_name', 'José'), ('last_name', 'Jiménez'), ('age', 42)]

        for key, value in DATA.items():
            print(f'key: "{key}", value: "{value}"')

        # key: "first_name", value: "José"
        # key: "last_name",  value: "Jiménez"
        # key: "age",        value: "42"

Iterating complex types
-----------------------
* flatmap

.. code-block:: python

    DATA = ['Max', ('1.0', 'José'), 3, 2.8, {True, None, False}]

    for element in DATA:
        print(f'value: "{element}"')

    # value: "Max"
    # value: "('1.0', 'José')"
    # value: "3"
    # value: "2.8"
    # value: "{False, True, None}"

.. code-block:: python

    DATA = ['Max', ('1.0', 'José'), 3, 2.8, {True, None, False}]

    for element in DATA:
        for sub in element:
            print(f'value: "{sub}"')

    # value: "M"
    # value: "a"
    # value: "x"
    # value: "1.0"
    # value: "José"
    # TypeError: 'int' object is not iterable


.. code-block:: python

    DATA = ['Max', ('1.0', 'José'), 3, 2.8, {True, None, False}]

    for element in DATA:

        if isinstance(element, (list, set, tuple)):
            for sub in element:
                print(f'value: "{sub}"')
        else:
            print(f'value: "{element}"')

    # value: "Max"
    # value: "1.0"
    # value: "José"
    # value: "3"
    # value: "2.8"
    # value: "False"
    # value: "True"
    # value: "None"


Assignments
===========

Text manipulation
-----------------
#. Dany jest tekst przemównienia John F. Kennedy'ego "Moon Speech" wygłoszony na Rice Stadium

    .. code-block:: text

        We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win

#. Dla każdego zdania (zdania oddzielone są kropkami)
#. Za pomocą funkcji ``len()`` policz ile jest wyrazów
#. Wypisz na ekranie listę słowników o strukturze: zdanie (klucz) -> ilość wyrazów (wartość)
#. Na końcu wypisz także ile jest zdań oraz ile słów i znaków naliczyliśmy łącznie

:About:
    * Filename: ``loop_sentences.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 10 min

:Co zadanie sprawdza:
    * Dzielenie stringów
    * Sprawdzanie długości ciągów znaków
    * Iterowanie po elementach listy

Unique keys from schema-less database
-------------------------------------
#. Mając bazę danych z listingu poniżej
#. Wygeneruj listę unikalnych kluczy dictów

.. code-block:: python

    DATABASE = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван', 'age': 42},
        {'first_name': 'Matt', 'last_name': 'Kowalski', 'born': 1961},
        {'first_name': 'José', 'born': 1961, 'agency': 'NASA'},
    ]

:Algorithm:
    #. Iteruj po rekordach w bazie danych
    #. Z rekordu wyciągnij klucze
    #. Dodaj klucze do zbioru
    #. Usuń duplikaty w zbiorze

:About:
    * Filename: ``loop_unique_keys.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Generowanie zbiorów
    * Usuwanie powtarzających się elementów
    * Wyciąganie elementów ze słownika
    * Iterowanie po słowniku
    * Aktualizacja zbiorów

Label encoder
-------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-loops-iris-sample`
#. Ze zbioru wyodrębnij dane odrzucając nagłówek.
#. Przemieszaj elementy zbioru danych
#. Stwórz słownik gatunków ``species``, gdzie kolejnym liczbom naturalnym zaczynając od zera przyporządkuj gatunek irysów.
#. Klucze muszą być wygenerowane na podstawie kolejności występowania gatunków w przemieszanym zbiorze danych:

    .. code-block:: python

        species = {
            0: 'versicolor',
            1: 'virginica',
            2: 'setosa'
        }

#. Przygotuj listę cech (``labels``) z kluczami ze słownika gatunków.
#. Etykiety muszą być wygenerowane na podstawie kolejności w przemieszanym zbiorze danych:

    .. code-block:: python

        print(labels)
        # [0, 1, 2, 1, 1, 0, ...]

#. Wyświetl na ekranie ``species`` oraz ``labels``

:Algorithm:
    #. Wyodrębnij dane odrzucając nagłówek
    #. Przemieszaj elementy zbioru danych
    #. Stwórz słownik gatunków ``species``
    #. Iteruj po elementach zbioru danych
    #. Gatunek to ostatni element rekordu
    #. Jeżeli w słowniku nie ma gatunku, to dodaj go z kolejnym numerem
    #. Do listy label dodawaj wartość słownika gatunków dla gatunku w tym rekordzie
    #. Odwróć słownik gatunków
    #. Wyświetl na ekranie ``species`` oraz ``labels``

:About:
    * Filename: ``loop_label_encoder.py``
    * Lines of code to write: 13 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Sprawdzanie występowania elementów w słowniku
    * Generowanie słownika i listy na podstawie innych danych
    * Odwracanie słownika

:Hints:
    * ``from random import shuffle``

.. literalinclude:: src/loops-iris-sample.py
    :name: listing-loops-iris-sample
    :language: python
    :caption: Sample Iris databases
