******************
Nested Collections
******************


``list`` of ``tuple``
=====================

Getting elements
----------------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    DATA[2]     # (7.6, 3.0, 6.6, 2.1, 'virginica')
    DATA[2][1]  # 3.0

Appending elements
------------------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    element = (4.9, 2.5, 4.5, 1.7, 'virginica')
    DATA.append(element)

    DATA.append((4.9, 3.0, 1.4, 0.2, 'setosa'))

Length
------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    len(DATA)       # 3
    len(DATA[2])    # 5


``list`` of ``dict``
====================

Getting elements
----------------
.. code-block:: python

    DATA = [
        {'first_name': 'Max'},
        {'first_name': 'José', 'last_name': 'Jiménez'},
        {'first_name': 'Иван', 'tags': ['astronaut', 'roscosmos', 'space']},
    ]

    DATA[0]                            # {'first_name': 'Max'}
    DATA[0]['last_name']               # KeyError: 'last_name'
    DATA[0].get('tags', 'n/a')         # 'n/a'
    DATA[2].get('tags')                # ['astronaut', 'roscosmos', 'space']
    DATA[2].get('tags')[1]             # 'roscosmos'

Length
------
.. code-block:: python

    DATA = [
        {'first_name': 'Max'},
        {'first_name': 'José', 'last_name': 'Jiménez'},
        {'first_name': 'Иван', 'tags': ['astronaut', 'roscosmos', 'space']},
    ]

    len(DATA)     # 3
    len(DATA[2])  # 2


``list`` of ``list``
====================
* Multidimensional lists

Readability counts
------------------
.. code-block:: python

    DATA = [[1,2,3],[4,5,6],[7,8,9]]

.. code-block:: python

    DATA = [[1,2,3], [4,5,6], [7,8,9]]

.. code-block:: python

    DATA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

Getting elements
----------------
.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    array[0][0]  # 1
    array[0][2]  # 3
    array[2][1]  # 8

Length
------
.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    len(DATA)     # 3
    len(DATA[2])  # 3

Mixed types
===========
.. code-block:: python

    DATA = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
        {'first_name': 'Pan', 'last_name': 'Twardowski'}
    ]

    DATA[1][2]                # 6
    DATA[3]['last_name']      # 'Twardowski'
    DATA[3].get('last_name')  # 'Twardowski'

.. code-block:: python

    DATA = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
        {'first_name': 'Pan', 'last_name': 'Twardowski'}
    ]

    len(DATA)     # 4
    len(DATA[2])  # 3
    len(DATA[3])  # 2


Assignments
===========

Split train/test
----------------
#. Mając do dyspozycji zbiór danych Irysów z listingu :numref:`listing-nested-iris-dataset`
#. Zapisz nagłówek (pierwsza linia) do zmiennej
#. Zapisz do innej zmiennej dane bez nagłówka
#. Wylicz punkt podziału: ilość rekordów danych bez nagłówka razy procent
#. Podziel zbiór na dwie listy w proporcji:

    - ``X_train`` - dane do uczenia - 60%
    - ``X_test`` - dane testowe - 40%

#. Z danych bez nagłówka zapisz do uczenia rekordy od początku do punktu podziału
#. Z danych bez nagłówka zapisz do testów rekordy od punktu podziału do końca

:About:
    * Filename: ``sequences_split_train_test.py``
    * Lines of code to write: 6 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Umiejętność przetwarzania złożonych typów danych
    * Korzystanie z przecięć danych
    * Konwersja typów
    * Magic Number

.. code-block:: python
    :caption: Iris Dataset
    :name: listing-nested-iris-dataset

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
        (7.1, 3.0, 5.9, 2.1, 'virginica'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.0, 3.6, 1.4, 0.3, 'setosa'),
        (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        (6.5, 3.0, 5.8, 2.2, 'virginica'),
        (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]
