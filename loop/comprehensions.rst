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

Comprehensions
--------------
.. code-block:: python

    [x for x in range(0, 5)]
    # list [10, 11, 12, 13, 14]


Inline ``for`` not only for ``list``
====================================

``set()``
---------
.. code-block:: python

    {x+10 for x in range(0, 5)}
    # set {10, 11, 12, 13, 14}

``dict()``
----------
.. code-block:: python

    {x: x+10 for x in range(0, 5)}
    # dict {0:10, 1:11, 2:12, 3:13, 4:14}

    {x+10: x for x in range(0, 5)}
    # dict {10:0, 11:1, 12:2, 13:3, 14:4}

    {x+10: x+10 for x in range(0, 5)}
    # dict {10:10, 11:11, 12:12, 13:13, 14:14}

``tuple()``
-----------
.. code-block:: python

    (x for x in range(0, 10))
    # <generator object <genexpr> at 0x11eaef570>


Conditional loop
================

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

    [x for x in range(0, 10) if x % 2 == 0]
    # [0, 2, 4, 6, 8]

Why?
====

Filtering results
-----------------
.. code-block:: python

    DATABASE = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    setosa = [x for x in DATA if x[4] == 'setosa']
    print(setosa)
    # [
    #   (5.1, 3.5, 1.4, 0.2, 'setosa'),
    #   (4.7, 3.2, 1.3, 0.2, 'setosa')
    # ]

Applying function to element
----------------------------
.. code-block:: python

    [float(x) for x in range(0, 10)]

.. code-block:: python

    [float(x) for x in range(0, 10) if x % 2 == 0]

.. code-block:: python

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    output = [float(x) for x in range(0, 10) if is_even(x)]

    print(output)
    # [0.0, 2.0, 4.0, 6.0, 8.0]

.. code-block:: python

    def get_tuple(number):
        return (number, number+10)

    output = [get_tuple(x) for x in range(0, 5)]

    print(output)
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

    output = [get_dict(x) for x in range(0, 5)]

    print(output)
    # [
    #    {'number': 0, 'status': 'even'},
    #    {'number': 1, 'status': 'odd'},
    #    {'number': 2, 'status': 'even'},
    #    {'number': 3, 'status': 'odd'},
    #    {'number': 4, 'status': 'even'},
    # ]


Examples
========

Reversing ``dict`` keys with values
-----------------------------------
.. code-block:: python

    my_dict = {'x': 1, 'y': 2}

    {value: key for key, value in my_dict.items()}
    # dict {1:'x', 2:'y'}

.. code-block:: python

    my_dict = {'x': 1, 'y': 2}

    {v:k for k,v in my_dict.items()}
    # dict {1:'x', 2:'y'}

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
    output = [x for x in line.split(':') if x.startswith('/')]

    print(output)
    # ['/home/jose', '/bin/bash']

Advanced usage for Comprehensions and Generators
------------------------------------------------
.. note:: More in chapter :ref:`Generators and Comprehensions`


Assignments
===========

Report card
-----------
#. Przekonwertuj skalę ocen ``(2, 3, 3.5, 4, 4.5, 5)`` na listę ``float`` za pomocą inline ``for``
#. Użytkownik podaje oceny jako ``int`` lub ``float``
#. Jeżeli ocena jest na liście dopuszczalnych ocen, dodaje ją do dzienniczka
#. Jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka
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
