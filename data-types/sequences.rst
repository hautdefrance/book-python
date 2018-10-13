.. _Data Structures:

******************
Simple Collections
******************


``list``
========
* Mutable - can add, remove, and modify values
* Defining with ``list()`` is more readable, but ``[]`` is used more often:

    .. code-block:: python

        my_list = []
        my_list = list()

* Brackets are required
* No need for comma for one element ``list``:

    .. code-block:: python

        my_list = [1]

* ``list`` can store elements of any types:

    .. code-block:: python

        my_list = [1, 2.0, None, False, 'José']

* You can also add ``list`` to ``list``:

    .. code-block:: python

        my_list = [1, 2.0, None, False, 'José', [1, 'hello']]

* Slicing, the same as for strings:

    .. code-block:: python

        my_list = [1, 2.0, None, False, 'José']

        my_list[1]             # 2.0
        my_list[2:4]           # [None, False]
        my_list[::2]           # [1, None, 'José']
        my_list[-1]            # 'José'

Adding ``list`` to ``list``
---------------------------
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

    len([1, 2, 3])  # 3
    len([])         # 0


``set``
=======
* Defining only with ``set()``:

    .. code-block:: python

        my_set = set()

* No need for comma for one element ``set``:

    .. code-block:: python

        my_set = {1}

* Only unique values:

    .. code-block:: python

        my_set = {1, 3, 1}          # {1, 3}

* Can store any hashable elements:

    .. code-block:: python

        my_set = {1, 2.0, 'Jose'}   # {1, 2.0, 'Jose'}
        my_set = {1, 2.0, [3, 4]}   # TypeError: unhashable type: 'list'
        my_set = {1, 2.0, {3, 4}}   # TypeError: unhashable type: 'set'

* Mutable - can add, remove, and modify values:

    .. code-block:: python

        my_set = {1, 2, 3}          # {1, 2, 3}

        my_set.add(4)               # {1, 2, 3, 4}
        my_set.add(4)               # {1, 2, 3, 4}
        my_set.add(3)               # {1, 2, 3, 4}

        my_set.update([4, 5])       # {1, 2, 3, 4, 5}
        my_set.update({4, 5})       # {1, 2, 3, 4, 5}

* Use of ``set`` operations with special syntax:

    .. code-block:: python

        {1,2} - {2,3}               # {1}        # Subtract
        {1,2} | {2,3}               # {1, 2, 3}  # Sum
        {1,2} & {2,3}               # {2}        # Union
        {1,2} ^ {2,3}               # {1, 3}     # Symmetrical difference
        {1,2} + {3,4}               # TypeError: unsupported operand type(s) for +: 'set' and 'set'

* Slicing ``set`` is not possible:

    .. code-block:: python

        my_set = {1, 2.0, None, False, 'José'}

        my_set[1]                   # TypeError: 'set' object does not support indexing
        my_set[2:4]                 # TypeError: 'set' object does not support indexing

* Length of a ``set``:

    .. code-block:: python

        my_set = {1, 2, 3}
        len(my_set)                 # 3

* Converting ``list`` to ``set`` deduplicate items:

    .. code-block:: python

        names = ['Matt', 'Иван', 'José', 'Matt']

        unique_names = set(names)
        # {'Matt', 'Иван', 'José'}

``tuple``
=========
* Immutable - cannot add, modify or remove elements
* Defining with ``tuple()`` is more readable, but ``()`` is used more often:

    .. code-block:: python

        my_tuple = ()
        my_tuple = tuple()

* Single element ``tuple`` require comma at the end (**important!**)
* Braces are optional:

    .. code-block:: python

        my_tuple = 1,
        my_tuple = (1,)

* Can store any type:

    .. code-block:: python

        my_tuple = 1, 2.0, None, False, 'José'
        my_tuple = (1, 2.0, None, False, 'José')

* Slicing tuple:

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)

        my_tuple[2]             # 3
        my_tuple[-1]            # 5
        my_tuple[:3]            # (1, 2, 3)
        my_tuple[3:]            # (4, 5)
        my_tuple[::2]           # (1, 3, 5)
        my_tuple[1:4]           # (2, 3, 4)

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)

        MIN = 1
        MAX = 4
        my_tuple[MIN:MAX]       # (2, 3, 4)

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)

        BETWEEN = slice(1, 4)
        my_tuple[BETWEEN]       # (2, 3, 4)

* Length of a ``tuple``:

    .. code-block:: python

        my_tuple = (1, 2, 3, 4, 5)
        len(my_tuple)           # 5


How Python understands types?
=============================
* Result of a ``type(what)`` for each line:

    .. code-block:: python

        what = 1.2        # <class 'float'>
        what = 1,2        # <class 'tuple'>

    .. code-block:: python

        what = 1, 2       # <class 'tuple'>
        what = (1, 2)     # <class 'tuple'>

    .. code-block:: python

        what = (1,2)      # <class 'tuple'>
        what = (1.2)      # <class 'float'>
        what = (1.2,)     # <class 'tuple'>

    .. code-block:: python

        what = 'foo'      # <class 'str'>
        what = ('foo')    # <class 'str'>

        what = 'foo',     # <class 'tuple'>
        what = ('foo',)   # <class 'tuple'>

    .. code-block:: python

        what = 1.        # <class 'float'>
        what = (1.)      # <class 'float'>

        what = .5        # <class 'float'>
        what = (.5)      # <class 'float'>

        what = 1.0       # <class 'float'>
        what = 1         # <class 'int'>

    .. code-block:: python

        what = 10.5      # <class 'float'>
        what = (10.5)    # <class 'float'>

        what = 10,5      # <class 'tuple'>
        what = (10,5)    # <class 'tuple'>

        what = 10.       # <class 'float'>
        what = (10.)     # <class 'float'>

        what = 10,       # <class 'tuple'>
        what = (10,)     # <class 'tuple'>

        what = 10        # <class 'int'>
        what = (10)      # <class 'int'>

    .. code-block:: python

        what = (1.,1.)   # <class 'tuple'>
        what = (.5,.5)   # <class 'tuple'>
        what = (1.,.5)   # <class 'tuple'>

        what = 1.,.5     # <class 'tuple'>


More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

Simple collections
------------------
#. Stwórz ``tuple`` z cyframi od 0-9
#. Przekonwertuj ją do ``list``
#. Na pierwsze miejsce w liście dodaj całą oryginalną ``tuple``
#. Przekonwertuj wszystko na płaski ``set`` unikalnych wartości wykorzystując ``slice``

:About:
    * Filename: ``sequences_conversions.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Rzutowanie i konwersja typów
