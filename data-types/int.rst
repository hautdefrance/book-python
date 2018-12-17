*******
``int``
*******


Defining ``int``
================
* Python 3 dynamically extends ``int``, when it's too big
* In Python 3 there is not maximal ``int`` value
* You can use ``_`` for easier read especially with big numbers

.. code-block:: python

    value = 30

.. code-block:: python

    million = 1000000
    million = 1_000_000


Converting to ``int``
=====================
* Also known as "type casting"
* ``int()`` converts argument to ``int``

.. code-block:: python

    int(10)          # 10

.. code-block:: python

    int(10.0)        # 10
    int(10.9)        # 10

    int(1.23)            # 1
    int(-1.23)           # -1

.. code-block:: python

    int('10')        # 10
    int('10.5')      # ValueError: invalid literal for int() with base 10: ' 10.5'


Numerical Operators
===================
.. csv-table:: Numerical types operators
    :header-rows: 1
    :widths: 15, 85
    :file: data/operators-numeric.csv
