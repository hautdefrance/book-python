.. _Comprehensions:

**************
Comprehensions
**************


Simple usage
============

Traditional
-----------
.. code-block:: python

    numbers = []

    for x in range(0, 5):
        numbers.append(x+10)

    # numbers = [10, 11, 12, 13, 14]

List Comprehension
------------------
.. code-block:: python

    [x+10 for x in range(0, 5)]
    # [10, 11, 12, 13, 14]

Set Comprehension
-----------------
.. code-block:: python

    {x+10 for x in range(0, 5)}
    # {10, 11, 12, 13, 14}

Dict Comprehension
------------------
.. code-block:: python

    {x: x+10 for x in range(0, 5)}
    # {0:10, 1:11, 2:12, 3:13, 4:14}

.. code-block:: python

    {x+10: x for x in range(0, 5)}
    # {10:0, 11:1, 12:2, 13:3, 14:4}

.. code-block:: python

    {x+10: x+10 for x in range(0, 5)}
    # {10:10, 11:11, 12:12, 13:13, 14:14}

Tuple Comprehension?!
---------------------
* It is a generator
* More in chapter :ref:`Generators and Comprehensions`

.. code-block:: python

    (x+10 for x in range(0, 5))
    # <generator object <genexpr> at 0x11eaef570>


Conditional Comprehension
=========================

Traditional
-----------
.. code-block:: python

    even_numbers = []

    for x in range(0, 10):
        if x % 2 == 0:
            even_numbers.append(x)

    print(even_numbers)
    # [0, 2, 4, 6, 8]

Comprehensions
--------------
.. code-block:: python

    even_numbers = [x for x in range(0, 10) if x % 2 == 0]

    print(even_numbers)
    # [0, 2, 4, 6, 8]


Why?
====

Filtering results
-----------------
.. code-block:: python

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    [record for record in DATA if record[4] == 'setosa']
    # [
    #   (5.1, 3.5, 1.4, 0.2, 'setosa'),
    #   (4.7, 3.2, 1.3, 0.2, 'setosa')
    # ]

Filtering with complex expressions
----------------------------------
.. code-block:: python

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]


    def is_setosa(record):
        if record[4] == 'setosa':
            return True
        else:
            return False


    [record for record in DATA if is_setosa(record)]
    # [
    #   (5.1, 3.5, 1.4, 0.2, 'setosa'),
    #   (4.7, 3.2, 1.3, 0.2, 'setosa')
    # ]

Applying function to each output element
----------------------------------------
.. code-block:: python

    [float(x) for x in range(0, 10)]

.. code-block:: python

    [float(x) for x in range(0, 10) if x % 2 == 0]

Returning nested objects
------------------------
.. code-block:: python

    def get_tuple(number):
        return number, number+10

    [get_tuple(x) for x in range(0, 5)]
    # [
    #   (0, 10),
    #   (1, 11),
    #   (2, 12),
    #   (3, 13),
    #   (4, 14)
    # ]

.. code-block:: python

    def get_dict(number):
        if number % 2 == 0:
            return {'number': number, 'status': 'even'}
        else:
            return {'number': number, 'status': 'odd'}


    [get_dict(x) for x in range(0, 5)]
    # [
    #    {'number': 0, 'status': 'even'},
    #    {'number': 1, 'status': 'odd'},
    #    {'number': 2, 'status': 'even'},
    #    {'number': 3, 'status': 'odd'},
    #    {'number': 4, 'status': 'even'},
    # ]

Reversing ``dict`` keys with values
-----------------------------------
.. code-block:: python

    DATA = {'a': 1, 'b': 2}

    DATA.items()
    # [
    #    ('a', 1),
    #    ('b', 2),
    # ]

.. code-block:: python

    DATA = {'a': 1, 'b': 2}

    {value: key for key, value in DATA.items()}
    # {1:'a', 2:'b'}

.. code-block:: python

    DATA = {'a': 1, 'b': 2}

    {v:k for k,v in DATA.items()}
    # {1:'a', 2:'b'}

Value collision while reversing ``dict``
----------------------------------------
.. code-block:: python

    DATA = {'a': 1, 'b': 2, 'c': 2}

    {v:k for k,v in DATA.items()}
    # {1:'a', 2:'c'}

Quick parsing lines
-------------------
.. code-block:: python

    line = 'jose:x:1000:1000:José Jiménez:/home/jose:/bin/bash'
    paths = []

    for record in line.split(':'):
        if record.startswith('/'):
            paths.append(record)

    print(paths)
    # ['/home/jose', '/bin/bash']

.. code-block:: python

    line = 'jose:x:1000:1000:José Jiménez:/home/jose:/bin/bash'
    paths = [x for x in line.split(':') if x.startswith('/')]

    print(paths)
    # ['/home/jose', '/bin/bash']


Advanced usage for Comprehensions and Generators
================================================
.. note:: More in chapter :ref:`Generators and Comprehensions`


Assignments
===========

Report card
-----------
#. Do zmiennej zapisz skalę ocen ``(2, 3, 3.5, 4, 4.5, 5)``
#. Przekonwertuj skalę na ``List[float]`` za pomocą inline List Comprehension
#. Użytkownik podaje oceny jako ``int`` lub ``float`` (nie będzie próbował psuć)
#. Jeżeli ocena jest na liście dopuszczalnych ocen, dodaj ją do dzienniczka
#. Jeżeli wciśnięto sam Enter, zakończ wpisywanie do dzienniczka
#. Jeżeli wpisano cyfrę nie znajdującą się na liście dopuszczalnych ocen, wyświetl informację "Grade is not allowed" i dalej kontynuuj wpisywanie
#. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną z ocen

:About:
    * Filename: ``loop_report_card.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 10 min

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
