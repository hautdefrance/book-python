*************************
Unpacking return elements
*************************


Operator ``*`` i ``**``
=======================
- To nie jest mnożenie i potęgowanie!
- ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
- ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane


Przypomnienie wiadomości o parametrach
======================================
.. code-block:: python

    def add(a, b):
        return a + b


    add(1, 2)       # pozycyjne
    add(a=1, b=2)   # nazwane, kolejność nie ma znaczenia
    add(b=2, a=1)   # nazwane, kolejność nie ma znaczenia
    add(1, b=2)     # pozycyjne i nazwane

.. code-block:: python

    a, b = 1, 2
    # a == 1
    # b == 2

    a, b = (1, 2)
    # a == 1
    # b == 2

    a, b = [1, 2]
    # a == 1
    # b == 2

.. code-block:: python

    def numbers():
        return [1, 2]

    a, b = numbers()
    # a == 1
    # b == 2


Przyjmowanie z funkcji zmiennej ilości argumentów (Rozpakowywanie)
==================================================================
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    line.split(',')
    # ['4.9', '3.1', '1.5', '0.1', 'setosa']

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    sepal_length, sepal_width, petal_length, petal_width, species = line.split(',')

    sepal_length    # '4.9'
    sepal_width     # '3.1'
    petal_length    # '1.5'
    petal_width     # '0.1'
    species         # 'setosa'

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    sepal_length, sepal_width, *others = line.split(',')

    sepal_length    # '4.9'
    sepal_width     # '3.1'
    others          # ['1.5', '0.1', 'setosa']

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *measurements, species = line.split(',')

    measurements    # ['4.9', '3.1', '1.5', '0.1']
    species         # 'setosa'

.. code-block:: python

    *a, b, *c = [4.9, 3.1, 1.5, 0.1, 'setosa']
    # SyntaxError: two starred expressions in assignment

.. code-block:: python

    # if you're not using ``measurements`` later in your code
    *_, species = line.split(',')

.. code-block:: python

    def get_iris():
        """
        Would be nice, if you can get ``dict``...
        but most programmers will return ``tuple``
        because it's a bit faster

        return {
            'sepal_length': 4.9,
            'sepal_width': 3.1,
            'petal_length': 1.5,
            'petal_width': 0.1,
            'species': 'setosa'
        }
        """
        return 4.9, 3.1, 1.5, 0.1, 'setosa'

    *measurements, species = get_iris()

