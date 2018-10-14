******************
Nested Collections
******************


``list`` of ``dict``
====================
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


Multidimensional lists
======================
* Readability counts:

    .. code-block:: python

        array = [[1,2,3],[4,5,6],[7,8,9]]
        array = [[1,2,3], [4,5,6], [7,8,9]]
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        array = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

* Getting element from nested lists:

    .. code-block:: python

        array = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        array[2][1]  # 8

Mixed types
===========
.. code-block:: python

    array = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
        {'first_name': 'José', 'last_name': 'Jiménez', 'age': 42}
    ]

    array[3]['last_name']  # 'Jiménez'


Assignments
===========

Split train/test
----------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-sequence-iris-sample`
#. Wyodrębnij nagłówek (pierwsza linia) od danych
#. Podziel zbiór na dwie listy w proporcji:

    - dane do uczenia - 80%
    - dane testowe - 20%

:Algorithm:
    #. zapisz nagłówek do zmiennej
    #. zapisz do innej zmiennej dane bez nagłówka
    #. wylicz punkt przegięcia: długość danych bez nagłówka razy procent
    #. z danych bez nagłówka zapisz do uczenia rekordy od początku do punktu przegięcia
    #. z danych bez nagłówka zapisz do testów rekordy od punktu przegięcia do końca

:About:
    * Filename: ``sequences_split_train_test.py``
    * Lines of code to write: 6 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Umiejętność przetwarzania złożonych typów danych
    * Korzystanie z przecięć danych
    * Konwersja typów
    * Magic Number

.. literalinclude:: assignment/sequence-iris-sample.py
    :name: listing-sequence-iris-sample
    :language: python
    :caption: Sample Iris databases
