*******
``set``
*******

* Can store elements of any **hashable** types
* Only unique values
* Mutable - can add, remove, and modify items
* Brackets are required
* Comma after last element is optional


Defining ``set``
================
* Defining only with ``set()``
* Is an unordered collection
* ``set`` do not record element position or order of insertion
* ``set`` do not support indexing, slicing, or other sequence-like behavior

Empty ``set``
-------------
.. code-block:: python

    my_set = set()

``set`` with one element
------------------------
.. code-block:: python

    my_set = {1}
    my_set = {1,}

``set`` with multiple values
----------------------------
.. code-block:: python

    my_set = {1, 3, 1}          # {1, 3}

``set`` with multiple values in many types
------------------------------------------
.. code-block:: python

    my_set = {1, 2.0, 'Jose'}   # {1, 2.0, 'Jose'}
    my_set = {1, 2.0, (3, 4)}   # {1, 2.0, (3, 4)}
    my_set = {1, 2.0, [3, 4]}   # TypeError: unhashable type: 'list'
    my_set = {1, 2.0, {3, 4}}   # TypeError: unhashable type: 'set'


Adding items
============

Adding one element
------------------
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


``set`` arithmetic
==================

``set.isdisjoint()``
--------------------
* Return True if the set has no elements in common with other.
* Sets are disjoint if and only if their intersection is the empty set.

.. code-block:: python

    {1,2}.isdisjoint({3,4})     # True

``set.issubset()``
------------------
* Test whether every element in the set is in other

.. code-block:: python

    {1,2} <= {3,4}              # False

.. code-block:: python

    {1,2} <= {1,2}              # True
    {1,2} <= {1,2,3}            # True

.. code-block:: python

    {1,2} < {1,2,3}             # True
    {1,2} < {1,2}               # False

``set.issuperset()``
--------------------
* Test whether every element in other is in the set

.. code-block:: python

    {1,2} > {1,2,3}             # False
    {1,2} > {1,2}               # False
    {1,2,3} > {1,2}             # True

.. code-block:: python

    {1,2} >= {1,2}              # True
    {1,2,3} >= {1,2}            # True

``set.union()``
---------------
* Return a new set with elements from the set and all others

.. code-block:: python

    {1,2} | {1,2}               # {1, 2}
    {1,2,3} | {1,2}             # {1, 2, 3}
    {1,2,3} | {1,2,4}           # {1, 2, 3, 4}
    {1,2} | {1,3} | {2,4}       # {1, 2, 3, 4}

``set.intersection()``
----------------------
* Return a new set with elements common to the set and all others

.. code-block:: python

    {1,2} & {2,3}               # {2}
    {1,2} & {2,3} & {2,4}       # {2}
    {1,2} & {2,3} & {3}         # set()

``str.difference()``
--------------------
* Return a new set with elements in the set that are not in the others

.. code-block:: python

    {1,2} - {2,3}               # {1}
    {1,2} - {2,3} - {3}         # {1}
    {1,2} - {1,2,3}             # set()

``set.symmetric_difference()``
------------------------------
* Return a new set with elements in either the set or other but not both

.. code-block:: python

    {1,2} ^ {1,2}               # set()
    {1,2} ^ {2,3}               # {1, 3}
    {1,2} ^ {1,3}               # {2, 3}


Slicing ``set``
===============
* Slicing ``set`` is not possible
* More in :ref:`Slice` chapter

.. code-block:: python

    my_set = {1, 2.0, None, False, 'José'}

    my_set[1]                   # TypeError: 'set' object does not support indexing
    my_set[2:4]                 # TypeError: 'set' object does not support indexing


Length of a ``set``
===================
.. code-block:: python

    my_set = {1, 2, 3}

    len(my_set)                 # 3


Converting ``list`` to ``set`` deduplicate items
================================================
.. code-block:: python

    names = ['Twardowski', 'Иван', 'Jiménez', 'Twardowski']

    unique_names = set(names)
    # {'Twardowski', 'Иван', 'Jiménez'}
