*****************************
Functions with many arguments
*****************************


.. note:: TL;DR:

    * ``*args`` unpack ``tuple`` or ``list``
    * ``**kwargs`` unpack ``dict``


Operators ``*`` i ``**``
========================
- To nie jest mnożenie i potęgowanie!
- ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
- ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane


Defining function with variable number of arguments
===================================================
- ``args`` - pozycyjne
- ``kwargs``- nazwane

.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *pozycyjne, **nazwane):
        print(f'argument a: {a}')                   # 1
        print(f'argument b: {b}')                   # 2
        print(f'argument c: {c}')                   # 3
        print(f'argumenty pozycyjne: {pozycyjne}')  # (4, 5, 6)
        print(f'argumenty nazwane: {nazwane}')      # {'d':7, 'e': 8}


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=7, e=8)

.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *args, **kwargs):
        print(f'argument a: {a}')                   # 1
        print(f'argument b: {b}')                   # 2
        print(f'argument c: {c}')                   # 3
        print(f'argumenty args: {args}')            # (4, 5, 6)
        print(f'argumenty kwargs: {kwargs}')        # {'d':7, 'e': 8}


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=7, e=8)


Case Study
==========
.. code-block:: python

    def celsius_to_fahrenheit(*degrees):
        return [degree*1.8+32 for degree in degrees]

    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]

