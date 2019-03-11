********
``list``
********

* Can store elements of any types
* Mutable - can add, remove, and modify items
* Brackets are required
* Comma after last element is optional


Defining ``list``
=================
* ``list()`` is more readable
* ``[]`` is used more often

Empty ``list``
--------------
.. code-block:: python

    my_list = []
    my_list = list()

One element ``list``
--------------------
.. code-block:: python

    my_list = [1]
    my_list = [1,]

Many element ``list``
---------------------
.. code-block:: python

    my_list = [1, 2.0, None, False, 'José']

.. code-block:: python

    alphabet = list('ABCDE')
    # ['A', 'B', 'C', 'D', 'E']

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


Adding elements
===============

``list`` arithmetic
-------------------
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

Multiple statements in one line
-------------------------------
.. code-block:: python

    my_list = [3, 1, 2]

    a = my_list.append(4).sort()
    # AttributeError: 'NoneType' object has no attribute 'sort'


Slicing ``list``
================
* Slicing works the same as for ``str``
* More in :ref:`Slice` chapter

.. code-block:: python

    my_list = [1, 2.0, None, False, 'José']

    my_list[1]             # 2.0
    my_list[2:4]           # [None, False]
    my_list[::2]           # [1, None, 'José']
    my_list[-1]            # 'José'


``sorted()`` vs. ``list.sort()``
================================

``sorted()``
------------
* ``sorted()`` zwraca posortowaną listę, ale nie zapisuje zmienionej kolejności

.. code-block:: python

    numbers = [3, 1, 2]

    sorted(numbers)     # returns [1, 2, 3]
    print(numbers)      # [3, 1, 2]

``list.sort()``
---------------
* ``list.sort()`` zmienia listę na stałe

.. code-block:: python

    numbers = [3, 1, 2]

    numbers.sort()      # returns None
    print(numbers)      # [1, 2, 3]


Built-in functions on sequences
===============================

``len()``
---------
.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    len(numbers)                   # 5
    len('Max')                     # 3

``min()``
---------
.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    min(numbers)  # 1
    min(3, 1, 5)  # 1

``max()``
---------
.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    max(numbers)  # 5
    max(3, 1, 5)  # 5

``sum()``
---------
.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    sum(numbers)  # 15
    sum(3, 1, 5)  # 9


Membership Operators
====================
.. csv-table:: Membership operators
    :widths: 15, 25, 60
    :header-rows: 1

    "Operand", "Example", "Description"
    "``x == y``", "``x == 18``", "value of ``x`` is equal to ``y``"
    "``x != y``", "``x != 18``", "value of ``x`` is not equal to ``y``"
    "``x in y``", "``x in [1, 2, 3]``", "``x`` contains ``y``"
    "``x not in y``", "``x not in [1, 2, 3]``", "``x`` not contains ``y``"


Length of a ``list``
====================
.. code-block:: python

    my_list = [1, 2, 3]

    len(my_list)    # 3
