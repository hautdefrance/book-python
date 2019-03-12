************************
Loops and nested objects
************************


Iterating over nested ``list`` items
====================================
.. code-block:: python
    :caption: Iterating over nested ``list`` items

    DATA = [1, 2, 3]

    for element in DATA:
        print(element)

    # 1
    # 2
    # 3

.. code-block:: python
    :caption: Iterating over nested ``list`` items

    DATA = [(...), (...), (...)]

    for element in DATA:
        print(element)

    # (...)
    # (...)
    # (...)

.. code-block:: python
    :caption: Iterating over nested ``list`` items

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

Unpacking values in loop
========================
.. code-block:: python
    :caption: Unpacking values in loop

    a, b = 'a', 0
    a, b = ('a', 0)
    k, v = ('a', 0)
    key, value = ('a', 0)
    sepal_len, sepal_wid, petal_len, petal_wid, species = (5.1, 3.5, 1.4, 0.2, 'setosa')

.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
    ]

    for key, value in DATA:
        print(f'key: "{key}", value: "{value}"')

    # a -> 0
    # b -> 1
    # c -> 2

.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (0, 1),
        ('name', 'José'),
        ('locations', ['CapeCanaveral', 'Houston']),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # 0 -> 1
    # name -> José
    # locations -> ['CapeCanaveral', 'Houston']

.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    # sepal_len, sepal_wid, petal_len, petal_wid, species = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for sepal_len, sepal_wid, petal_len, petal_wid, species in DATA:
        print(species)

    # setosa
    # versicolor
    # virginica

Enumerating and item index
==========================
.. code-block:: python
    :caption: Enumerating and item index

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    i = 0

    for element in DATA:
        print(f'{i} -> {element}')
        i += 1

    # 0 -> (5.1, 3.5, 1.4, 0.2, 'setosa')
    # 1 -> (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # 2 -> (6.3, 2.9, 5.6, 1.8, 'virginica')


.. code-block:: python
    :caption: Enumerating and item index

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for i, element in enumerate(DATA):
        print(f'{i} -> {element}')

    # 0 -> (5.1, 3.5, 1.4, 0.2, 'setosa')
    # 1 -> (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # 2 -> (6.3, 2.9, 5.6, 1.8, 'virginica')


Iterating over ``dict`` items
=============================
* ``dict`` elements order changes!

Iterating over ``dict`` values
------------------------------
.. code-block:: python
    :caption: Iterating over ``dict`` items

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

Iterating over ``dict`` keys
----------------------------
.. code-block:: python
    :caption: Iterating over ``dict`` items

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

By default ``dict`` iterates over keys
--------------------------------------
.. code-block:: python
    :caption: By default ``dict`` iterates over keys

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

Getting pair: ``key``, ``value`` from ``dict`` items
----------------------------------------------------
.. code-block:: python
    :caption: Getting pair: ``key``, ``value`` from ``dict`` items

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

``list`` of ``dict``
--------------------
.. code-block:: python
    :caption: ``list`` of ``dict``

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

    for row in DATA:
        print(row['Species'])

    # setosa
    # versicolor
    # virginica


Iterating complex types
=======================
.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - simple loop

    DATA = ['Max', ('1.0', 'José'), 3, 2.8, {True, None, False}]

    for element in DATA:
        print(f'value: "{element}"')

    # value: "Max"
    # value: "('1.0', 'José')"
    # value: "3"
    # value: "2.8"
    # value: "{False, True, None}"

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - nested loop

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
    :caption: Iterating over ``list`` with scalar and vector values - smart loop

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

Unique keys from schema-less database
-------------------------------------
* Filename: ``loop_unique_keys.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Input data: :numref:`listing-loops-unique-keys`

#. Mając bazę danych z listingu poniżej
#. Iteruj po rekordach w bazie danych
#. Z rekordu wyciągnij klucze
#. Wypisz unikalne klucze

.. code-block:: python
    :name: listing-loops-unique-keys
    :caption: Unique keys from schema-less database

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

:The whys and wherefores:
    * Generowanie zbiorów
    * Usuwanie powtarzających się elementów
    * Wyciąganie elementów ze słownika
    * Iterowanie po słowniku
    * Aktualizacja zbiorów

Label encoder
-------------
* Filename: ``loop_label_encoder.py``
* Lines of code to write: 13 lines
* Estimated time of completion: 15 min
* Input data: :numref:`listing-loops-iris-sample`

.. literalinclude:: src/loops-iris-sample.py
    :name: listing-loops-iris-sample
    :language: python
    :caption: Sample Iris databases

#. Ze zbioru :numref:`listing-loops-iris-sample` wyodrębnij dane odrzucając nagłówek
#. Z danych wyodrębnij:

    * cechy opisujące: ``features: List[Tuple[float]]``
    * cechy opisywane: ``labels: List[int]``

#. Przykład danych wyodrębnionych:

    .. code-block:: python
        :caption: Przykład danych wyodrębnionych

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
        :caption: Przykład słownika ``species``

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

:The whys and wherefores:
    * Sprawdzanie występowania elementów w słowniku
    * Generowanie słownika i listy na podstawie innych danych
    * Odwracanie słownika
