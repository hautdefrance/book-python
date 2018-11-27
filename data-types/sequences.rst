.. _Data Structures:

******************
Simple Collections
******************


``list``
========
* Can store elements of any types
* Mutable - can add, remove, and modify items
* Brackets are required
* Comma after last element is optional

Defining ``list``
-----------------
* ``list()`` is more readable
* ``[]`` is used more often

.. code-block:: python

    my_list = []
    my_list = list()

.. code-block:: python

    my_list = [1]
    my_list = [1,]

.. code-block:: python

    my_list = [1, 2.0, None, False, 'José']

Nested ``list``
---------------
.. code-block:: python

    my_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

.. code-block:: python

    my_list = [1, 2.0, [1, 'hello'], None, [2, 1]]

Slicing ``list``
----------------
* Slicing works the same as for ``str``

.. code-block:: python

    my_list = [1, 2.0, None, False, 'José']

    my_list[1]             # 2.0
    my_list[2:4]           # [None, False]
    my_list[::2]           # [1, None, 'José']
    my_list[-1]            # 'José'

Adding elements
---------------
.. code-block:: python

    my_list = [1, 2]

    my_list + [3, 4]        # [1, 2, 3, 4]

Appending elements
------------------
.. code-block:: python

    my_list = [1, 2]

    my_list.append(3)       # [1, 2, 3]
    my_list.append([4, 5])  # [1, 2, 3, [4, 5]]

Extending lists
---------------
.. code-block:: python

    my_list = [1, 2]

    my_list.extend([3, 4])  # [1, 2, 3, 4]

Inserting elements at specific position
---------------------------------------
.. code-block:: python

    my_list = [1, 2]

    my_list.insert(0, 'a')  # ['a', 1, 2]

Length of a ``list``
--------------------
.. code-block:: python

    my_list = [1, 2, 3]

    len(my_list)    # 3


``set``
=======
* Can store elements of any **hashable** types
* Only unique values
* Mutable - can add, remove, and modify items
* Brackets are required
* Comma after last element is optional

Defining ``set``
----------------
* Defining only with ``set()``

.. code-block:: python

    my_set = set()

.. code-block:: python

    my_set = {1}
    my_set = {1,}

.. code-block:: python

    my_set = {1, 3, 1}          # {1, 3}

.. code-block:: python

    my_set = {1, 2.0, 'Jose'}   # {1, 2.0, 'Jose'}
    my_set = {1, 2.0, [3, 4]}   # TypeError: unhashable type: 'list'
    my_set = {1, 2.0, {3, 4}}   # TypeError: unhashable type: 'set'

Adding items
------------
.. code-block:: python

    my_set = {1, 2, 3}          # {1, 2, 3}

    my_set.add(4)               # {1, 2, 3, 4}
    my_set.add(4)               # {1, 2, 3, 4}
    my_set.add(3)               # {1, 2, 3, 4}

Adding many items
-----------------
.. code-block:: python

    my_set = {1, 2, 3}          # {1, 2, 3}

    my_set.update([4, 5])       # {1, 2, 3, 4, 5}

.. code-block:: python

    my_set = {1, 2, 3}          # {1, 2, 3}

    my_set.update({4, 5})       # {1, 2, 3, 4, 5}

Mathematical ``set`` operations
-------------------------------
.. code-block:: python

    {1,2} - {2,3}    # {1}        # Subtract
    {1,2} | {2,3}    # {1, 2, 3}  # Sum
    {1,2} & {2,3}    # {2}        # Union
    {1,2} ^ {2,3}    # {1, 3}     # Symmetrical difference
    {1,2} + {3,4}    # TypeError: unsupported operand type(s) for +: 'set' and 'set'

Slicing ``set``
---------------
* Slicing ``set`` is not possible

.. code-block:: python

    my_set = {1, 2.0, None, False, 'José'}

    my_set[1]                   # TypeError: 'set' object does not support indexing
    my_set[2:4]                 # TypeError: 'set' object does not support indexing

Length of a ``set``
-------------------
.. code-block:: python

    my_set = {1, 2, 3}

    len(my_set)                 # 3

Converting ``list`` to ``set`` deduplicate items
------------------------------------------------
.. code-block:: python

    names = ['Matt', 'Иван', 'José', 'Matt']

    unique_names = set(names)
    # {'Matt', 'Иван', 'José'}


``tuple``
=========
* Can store elements of any types
* Immutable - cannot add, modify or remove items
* Brackets are optional
* Comma after last element is optional
* Single element ``tuple`` require comma at the end (**important!**)

Defining ``tuple``
------------------
* ``tuple()`` is more readable
* ``()`` is used more often

.. code-block:: python

    my_tuple = ()
    my_tuple = tuple()

.. code-block:: python

    my_tuple = 1,
    my_tuple = (1,)

.. code-block:: python

    my_tuple = 1, 2
    my_tuple = (1, 2)

.. code-block:: python

    my_tuple = 1, 2.0, None, False, 'José'
    my_tuple = (1, 2.0, None, False, 'José')

Slicing ``tuple``
-----------------
.. code-block:: python

    my_tuple = (1, 2, 3, 4, 5)

    my_tuple[2]             # 3
    my_tuple[-1]            # 5
    my_tuple[:3]            # (1, 2, 3)
    my_tuple[3:]            # (4, 5)
    my_tuple[::2]           # (1, 3, 5)
    my_tuple[1:4]           # (2, 3, 4)

Length of a ``tuple``
---------------------
.. code-block:: python

    my_tuple = (1, 2, 3)

    len(my_tuple)           # 3


Unpacking sequences to variables
================================
.. code-block:: python

    a, b, c = 1, 2, 3
    a, b, c = (1, 2, 3)
    a, b, c = [1, 2, 3]
    a, b, c = {1, 2, 3}


How Python understands types?
=============================
.. code-block:: python

    what = 1.2        # float
    what = 1,2        # tuple

    what = (1.2)      # float
    what = (1,2)      # tuple

.. code-block:: python

    what = 1.2,       # tuple with float
    what = 1,2.3      # tuple with int and float

    what = (1.2,)     # tuple with float
    what = (1,2.3)    # tuple with int and float

.. code-block:: python

    what = 'foo'      # str
    what = 'foo',     # tuple with str
    what = 'foo'.     # SyntaxError: invalid syntax

    what = ('foo')    # str
    what = ('foo',)   # tuple with str
    what = ('foo'.)   # SyntaxError: invalid syntax

.. code-block:: python

    what = 1.        # float
    what = .5        # float
    what = 1.0       # float
    what = 1         # int

    what = (1.)      # float
    what = (.5)      # float
    what = (1.0)     # float
    what = (1)       # int

.. code-block:: python

    what = 10.5      # float
    what = 10,5      # tuple with two ints
    what = 10.       # float
    what = 10,       # tuple with int
    what = 10        # int

    what = (10.5)    # float
    what = (10,5)    # tuple with two ints
    what = (10.)     # float
    what = (10,)     # tuple with int
    what = (10)      # int

.. code-block:: python

    what = 1.,1.     # tuple with two floats
    what = .5,.5     # tuple with two floats
    what = 1.,.5     # tuple with two floats

    what = (1.,1.)   # tuple with two floats
    what = (.5,.5)   # tuple with two floats
    what = (1.,.5)   # tuple with two floats


Membership Operators
====================
.. csv-table:: Membership operators
    :header-rows: 1
    :widths: 15, 25, 60
    :file: data/operators-membership.csv


More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

Iris dataset
------------
#. Mając dane z listingu poniżej, za pomocą slice wyodrębnij...
#. Zmienną ``features: List[Tuple[float]]`` z wynikami pomiarów
#. Zmienną ``labels: List[str]``, która będzie zawierała w kolejności wszystkie nazwy gatunków
#. Zmienną ``species: Set[str]``, która jest unikalnym zbiorem gatunków (na podstawie ``labels``)

.. code-block:: python

    DATABASE = (
        5.8, 2.7, 5.1, 1.9, 'virginica',
        5.1, 3.5, 1.4, 0.2, 'setosa',
        5.7, 2.8, 4.1, 1.3, 'versicolor',
        6.3, 2.9, 5.6, 1.8, 'virginica',
        6.4, 3.2, 4.5, 1.5, 'versicolor',
        4.7, 3.2, 1.3, 0.2, 'setosa',
    )

.. code-block:: python

    features = [
        (5.8, 2.7, 5.1, 1.9),
        (5.1, 3.5, 1.4, 0.2),
        (5.7, 2.8, 4.1, 1.3),
        (6.3, 2.9, 5.6, 1.8),
        (6.4, 3.2, 4.5, 1.5),
        (4.7, 3.2, 1.3, 0.2),
    ]

    labels = [
        'virginica',
        'setosa',
        'versicolor',
        'virginica',
        'versicolor',
        'setosa',
    ]

    species = {
        'versicolor',
        'setosa',
        'virginica',
    }

:About:
    * Filename: ``sequences_iris.py``
    * Lines of code to write: 30 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Slice zbiorów danych
    * Rzutowanie i konwersja typów


Simple collections
------------------
#. Stwórz ``tuple`` z cyframi 0, 1, 2, 3
#. Przekonwertuj ją do ``list``
#. Na pierwsze miejsce w liście dodaj całą oryginalną ``tuple``
#. Przekonwertuj wszystko na płaski ``set`` unikalnych wartości wykorzystując ``slice``

:About:
    * Filename: ``sequences_conversions.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Slice zbiorów danych
    * Rzutowanie i konwersja typów
