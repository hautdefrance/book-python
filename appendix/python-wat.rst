************
Python WAT?!
************

.. code-block:: python

    list('ABCDE')
    # ['A', 'B', 'C', 'D', 'E']

    list('ABCDE',)
    # ['A', 'B', 'C', 'D', 'E']

    list('ABCDE','asd')
    # Traceback (most recent call last):
    #  File "<input>", line 1, in <module>
    # TypeError: list expected at most 1 arguments, got 2

    a = 'ABCDE'
    list(a)
    # ['A', 'B', 'C', 'D', 'E']

    a = 'ABCDE',
    list(a)
    # ['ABCDE']

    a = ('ABCDE',)
    list(a)
    # ['ABCDE']

.. code-block:: python

    999 + 1 is 1000         # False
    1000 is 1000            # True

* Ze względów optymalizacyjnych od którejś wartości, obiekty mają inną tożsamość
.. code-block:: python

    1 + 1 is 2              # True
    0.1 + 0.2 is 0.3        # False

.. code-block:: python

    2.2 * 3.0 == 3.3 * 2.0  # False

.. code-block:: python

    for x in ('hello'):
        print(x)
    # h
    # e
    # l
    # l
    # o

    for x in ('hello',):
        print(x)
    # hello

    for x in 'hello':
        print(x)
    # h
    # e
    # l
    # l
    # o

    for x in 'hello',:
        print(x)
    # hello

.. code-block:: python

    a = [1, 2, 3]
    x = a

    print(x)  # [1, 2, 3]
    print(a)  # [1, 2, 3]

    x.append(4)

    print(x)  # [1, 2, 3, 4]
    print(a)  # [1, 2, 3, 4]

.. code-block:: python

    a = [1, 2, 3]
    x = a

    x = a.copy()
    x.append(4)

    print(x)  # [1, 2, 3, 4]
    print(a)  # [1, 2, 3]

