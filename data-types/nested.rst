******************
Nested Collections
******************


``list`` of ``tuple``
====================

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
-------------
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
#. Mając do dyspozycji zbiór danych Irysów z listingu poniżej:

    .. literalinclude:: assignment/sequence-iris-sample.py
        :language: python
        :caption: Sample Iris databases

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
