.. _Generators and Comprehensions:

*****************************
Generators and Comprehensions
*****************************


Lazy evaluation
===============
* Code do not execute instantly
* Sometimes code is not executed at all!

Declaring generators
--------------------
.. code-block:: python

    # This will not execute code!
    range(0, 9_999_999)
    range(0, 9_999_999)
    range(0, 9_999_999)

.. code-block:: python

    # This will only create generator expression, but not execute it!
    numbers = range(0, 9_999_999)
    print(numbers)
    # range(0, 9999999)

Getting  values from generator
------------------------------
.. code-block:: python

    numbers = range(0, 9_999_999)
    list(range)  # Generator will execute here (not very efficient)

.. code-block:: python

    # Generator will execute once at a time, for every loop iteration
    for i in range(0, 9_999_999):
        print(i)


Generator expressions vs. Comprehensions
========================================

Comprehensions
--------------
* Executes instantly

.. code-block:: python

    a = [x for x in range(0, 10)]
    b = {x for x in range(0, 10)}
    c = {x: x for x in range(0, 10)}

.. code-block:: python

    d = list(x for x in range(0, 10))
    e = set(x for x in range(0, 10))
    f = dict(x: x for x in range(0, 10))
    g = tuple(x for x in range(0, 10))

Generator Expressions
---------------------
* Lazy evaluation

.. code-block:: python

    i = (x*x for x in range(0, 30) if x % 2)

What is the difference?
-----------------------
.. code-block:: python

    # tutaj nastąpi wykonanie i przypisanie
    numbers = [x**2 for x in range(0, 30) if x % 2 == 0]

    print(numbers)
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]

    print(numbers)
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]

.. code-block:: python

    # tu nastąpi tylko przypisanie do generatora
    numbers = (x**2 for x in range(0, 30) if x % 2 == 0)

    print(numbers)
    # <generator object <genexpr> at 0x11af5a570>

    print(list(numbers))
    # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784]

    print(list(numbers))
    # []

Which one is better?
--------------------
* Comprehensions - Using values more than one
* Generators - Using value one (for example in the loop iterator)

Nested Comprahensions
---------------------
.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Matt', 'last_name': 'Kowalski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    fieldnames = set()
    fieldnames.update(key for record in DATA for key in record.keys())


Readability counts
------------------
.. literalinclude:: src/generator-clean-code.py
    :name: listing-generator-clean-code
    :language: python
    :caption: Clean Code in generator


Operator ``yield``
==================
.. code-block:: python

    # ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

.. code-block:: python

    def get_species(species):
        output = []

        for record in DATA:
            if record[4] == species:
                output.append(record)

        return output


    data = get_species('setosa')

    print(data)
    # [(5.1, 3.5, 1.4, 0.2, 'setosa'),
    #  (4.9, 3.0, 1.4, 0.2, 'setosa'),
    #  (5.4, 3.9, 1.7, 0.4, 'setosa'),
    #  (4.6, 3.4, 1.4, 0.3, 'setosa')]


    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')
    # (4.6, 3.4, 1.4, 0.3, 'setosa')


.. code-block:: python

    def get_species(species):
        for record in DATA:
            if record[4] == species:
                yield record

    data = get_species('setosa')

    print(data)
    # <generator object get_species at 0x11af257c8>


    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')
    # (4.6, 3.4, 1.4, 0.3, 'setosa')


The whys and wherefores
=======================

Filtering ``list`` items
------------------------
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

    setosa = [x for x in DATA if x[4] == 'setosa']
    print(setosa)

Filtering ``dict`` items
------------------------
.. code-block:: python

    DATA = [
        {'first_name': 'Иван', 'last_name': 'Иванович', 'agency': 'Roscosmos'},
        {'first_name': 'Jose', 'last_name': 'Jimenez', 'agency': 'NASA'},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'agency': 'NASA'},
        {'first_name': 'Alex', 'last_name': 'Vogel', 'agency': 'ESA'},
        {'first_name': 'Mark', 'last_name': 'Watney', 'agency': 'NASA'},
    ]

    nasa_astronauts = [(astronaut['first_name'], astronaut['last_name']) for astronaut in DATA if astronaut['agency'] == 'NASA']
    # [
    #   ('Jose', 'Jimenez'),
    #   ('Melissa', 'Lewis'),
    #   ('Mark', 'Watney')
    # ]

    nasa_astronauts = [(x['first_name'], x['last_name']) for x in DATA if x['agency'] == 'NASA']
    # [
    #   ('Jose', 'Jimenez'),
    #   ('Melissa', 'Lewis'),
    #   ('Mark', 'Watney')
    # ]

Reversing ``dict`` keys with values
-----------------------------------
.. code-block:: python

    data = {'first_name': 'Иван', 'last_name': 'Иванович'}

    {v: k for k, v in data.items()}
    # dict {'Иван': 'first_name', 'Иванович': 'last_name'}

Applying functions
------------------
.. code-block:: python

    [float(x) for x in range(0, 10) if x % 2 == 0]
    # [0.0, 2.0, 4.0, 6.0, 8.0]

.. code-block:: python

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    [float(x) for x in range(0, 10) if is_even(x)]
    # [0.0, 2.0, 4.0, 6.0, 8.0]


Assignments
===========

Generators vs. Comprehensions - iris
------------------------------------
* Filename: ``generator_iris.py``
* Lines of code to write: 40 lines
* Estimated time of completion: 20 min
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/database/data/iris.csv

#. Skopiuj dane do pliku "iris.csv"
#. Zaczytaj dane pomijając nagłówek
#. Napisz funkcję która zwraca wszystkie pomiary dla danego gatunku
#. Gatunek będzie podawany jako ``str`` do funkcji
#. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
#. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``

:The whys and wherefores:
    * Wykorzystanie generatorów
    * Odbieranie danych z lazy evaluation
    * Porównanie wielkości struktur danych
    * Parsowanie pliku
    * Filtrowanie treści w locie

Generators vs. Comprehensions - passwd
--------------------------------------
* Filename: ``generator_passwd.py``
* Lines of code to write: 40 lines
* Estimated time of completion: 20 min

#. Napisz program, który wczyta plik :numref:`listing-file-etc-passwd-2`
#. Przefiltruj linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``) oraz pustych linii
#. Przefiltruj linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
#. Zwróć listę loginów użytkowników systemowych
#. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
#. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
#. Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

:The whys and wherefores:
    * Wykorzystanie generatorów
    * Odbieranie danych z lazy evaluation
    * Porównanie wielkości struktur danych
    * Parsowanie pliku
    * Filtrowanie treści w locie

.. literalinclude:: assignment/etc-passwd.txt
    :name: listing-file-etc-passwd-2
    :language: text
    :caption: ``/etc/passwd`` sample file
