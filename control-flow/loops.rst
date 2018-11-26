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
        print(i)
        i += 1


``for``
=======

Iterating over ``str``
----------------------
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
----------------------------
* Iterating over ``list``:

    .. code-block:: python

        DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']

        for element in DATA:
            print(element)

        # 5.1
        # 3.5
        # 1.4
        # 0.2
        # 'setosa'

* Iterating over ``tuple``:

    .. code-block:: python

        DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

        for element in DATA:
            print(element)

        # 5.1
        # 3.5
        # 1.4
        # 0.2
        # 'setosa'

* Iterating over ``set``:

    .. code-block:: python

        DATA = {5.1, 3.5, 1.4, 0.2, 'setosa'}

        for element in DATA:
            print(element)

        # 5.1
        # 3.5
        # 1.4
        # 0.2
        # 'setosa'

* ``range(0, 5)`` will generate ``(0, 1, 2, 3, 4)``

    .. code-block:: python

        for number in range(0, 5):
            print(number)

        # 0
        # 1
        # 2
        # 3
        # 4

Iterating over nested ``list`` items
------------------------------------
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for element in DATA:
        print(element)

    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # (6.3, 2.9, 5.6, 1.8, 'virginica')

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

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for element in DATA:
        print(element)

    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # (6.3, 2.9, 5.6, 1.8, 'virginica')

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for i, element in enumerate(DATA):
        print(i, element)

    # 0 (5.1, 3.5, 1.4, 0.2, 'setosa')
    # 1 (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # 2 (6.3, 2.9, 5.6, 1.8, 'virginica')


Iterating over ``dict`` items
-----------------------------
* ``dict`` elements order changes!
* Iterating over ``dict`` values:

    .. code-block:: python

        DATA = {
            'Sepal length': 5.1,
            'Sepal width': 3.5,
            'Petal length': 1.4,
            'Petal width': 0.2,
            'Species': 'setosa',
        }

        DATA.values()
        # [5.1, 3.5, 1.4, 0.2, 'setosa']

        for element in DATA.values():
            print(element)

        # 5.1
        # 3.5
        # 1.4
        # 0.2
        # 'setosa'

* Iterating over ``dict`` keys:

    .. code-block:: python

        DATA = {
            'Sepal length': 5.1,
            'Sepal width': 3.5,
            'Petal length': 1.4,
            'Petal width': 0.2,
            'Species': 'setosa',
        }

        DATA.keys()
        # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']

        for element in DATA.keys():
            print(element)

        # 'Sepal length'
        # 'Sepal width'
        # 'Petal length'
        # 'Petal width'
        # 'Species'

* By default ``dict`` iterates over keys:

    .. code-block:: python

        DATA = {
            'Sepal length': 5.1,
            'Sepal width': 3.5,
            'Petal length': 1.4,
            'Petal width': 0.2,
            'Species': 'setosa',
        }

        for element in DATA:
            print(element)

        # 'Sepal length'
        # 'Sepal width'
        # 'Petal length'
        # 'Petal width'
        # 'Species'

* Getting pair: ``key``, ``value`` from ``dict`` items:

    .. code-block:: python

        DATA = {
            'Sepal length': 5.1,
            'Sepal width': 3.5,
            'Petal length': 1.4,
            'Petal width': 0.2,
            'Species': 'setosa',
        }

        DATA.items()
        # [
        #   ('Sepal length', 5.1),
        #   ('Sepal width', 3.5),
        #   ('Petal length', 1.4),
        #   ('Petal width', 0.2),
        #   ('Species', 'setosa')
        # ]


        for key, value in DATA.items():
            print(f'{key} -> {value}')

        # Sepal length -> 5.1
        # Sepal width -> 3.5
        # Petal length -> 1.4
        # Petal width -> 0.2
        # Species -> setosa

Iterating complex types
-----------------------
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
#. Dany jest tekst przemównienia John F. Kennedy'ego "Moon Speech" wygłoszony na Rice Stadium (zdania oddzielone są kropkami)

    .. code-block:: text

        We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win

#. Każde zdanie oczyść z białych znaków na początku i końcu
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
#. Dany jest zbiór pomiarów Irysów :numref:`listing-loops-iris-sample`
#. Ze zbioru wyodrębnij dane odrzucając nagłówek
#. Z danych wyodrębnij:

    * cechy opisujące: ``features: List[Tuple[float]]``
    * cechy opisywane: ``labels: List[int]``

#. Przykład danych wyodrębnionych:

    .. code-block:: python

        features = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2), ...]

        labels = [0, 1, 2, 1, 2, 0, ...]

#. Aby móc odszyfrować ``labels`` i zamienić wartości na nazwy gatunków, potrzebny jest słownik podmiany "liczba -> nazwa"
#. Wygeneruj słownik ``species: Dict[int, str]`` na podstawie danych
#. Przykład słownika ``species``:

    .. code-block:: python

        species = {
            0: 'virginica',
            1: 'setosa',
            2: 'versicolor'
        }

#. Wyświetl na ekranie:

    * ``species``
    * ``labels``
    * ``features``

:Algorithm:
    #. Wyodrębnij dane odrzucając nagłówek
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

.. literalinclude:: src/loops-iris-sample.py
    :name: listing-loops-iris-sample
    :language: python
    :caption: Sample Iris databases
