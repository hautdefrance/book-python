*********
``tuple``
*********

* Can store elements of any types
* Immutable - cannot add, modify or remove items
* Brackets are optional
* Comma after last element is optional
* Single element ``tuple`` require comma at the end (**important!**)


Defining ``tuple``
==================
* ``tuple()`` is more readable
* ``()`` is used more often

Empty ``tuple``
---------------
.. code-block:: python

    my_tuple = ()
    my_tuple = tuple()

``tuple`` with one element
--------------------------
.. code-block:: python

    my_tuple = 1,
    my_tuple = (1,)

``tuple`` with many elements
----------------------------
.. code-block:: python

    my_tuple = 1, 2
    my_tuple = (1, 2)

.. code-block:: python

    my_tuple = 1, 2.0, None, False, 'José'
    my_tuple = (1, 2.0, None, False, 'José')


Slicing ``tuple``
=================
* More in :ref:`Slice` chapter

.. code-block:: python

    my_tuple = (1, 2, 3, 4, 5)

    my_tuple[2]             # 3
    my_tuple[-1]            # 5
    my_tuple[:3]            # (1, 2, 3)
    my_tuple[3:]            # (4, 5)
    my_tuple[::2]           # (1, 3, 5)
    my_tuple[1:4]           # (2, 3, 4)


Length of a ``tuple``
=====================
.. code-block:: python

    my_tuple = (1, 2, 3)

    len(my_tuple)           # 3
