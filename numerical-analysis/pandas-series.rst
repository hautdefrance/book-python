*****************
Pandas ``Series``
*****************


.. warning:: Following values are generated with ``np.random.seed(0)``

Values
======
.. code-block:: python

    pd.Timestamp('1961-04-12')
    pd.Categorical(["test", "train", "test", "train"])


Creating
========
* 1-dimentional data structure similar to ``ndarray``

.. code-block:: python

    values = [1, 3, 5, np.nan, 6, 8]

    pd.Series(values)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64


Indexes
=======

Numbered
--------
* by default

.. code-block:: python

    values = [1, 3, 5, np.nan, 6, 8]

    pd.Series(values)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64

Alphabetic
----------
.. code-block:: python

    indexes = ['a', 'b', 'c', 'd', 'e', 'f']
    values = [1, 3, 5, np.nan, 6, 8]

    s = pd.Series(values, index=indexes)
    # a    1.0
    # b    3.0
    # c    5.0
    # d    NaN
    # e    6.0
    # f    8.0
    # dtype: float64

.. code-block:: python

    values = np.random.randn(5)

    s = pd.Series(values, index=list('abcdef'))
    # a    1.0
    # b    3.0
    # c    5.0
    # d    NaN
    # e    6.0
    # f    8.0
    # dtype: float64

Datetime
--------
* Default is "Daily"

.. code-block:: python

    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    values = [1, 3, 5, np.nan, 6, 8]

    s = pd.Series(values, index=indexes)
    # 1970-01-01    1.0
    # 1970-01-02    3.0
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # 1970-01-06    8.0
    # Freq: D, dtype: float64

Every year
^^^^^^^^^^
.. code-block:: python

    pd.date_range('1970-01-01', periods=6, freq='Y')
    # DatetimeIndex(['1970-12-31',
    #                '1971-12-31',
    #                '1972-12-31',
    #                '1973-12-31',
    #                '1974-12-31',
    #                '1975-12-31'],
    #                dtype='datetime64[ns]', freq='A-DEC')

Every month
^^^^^^^^^^^
.. code-block:: python

    pd.date_range('1970-01-01', periods=6, freq='Y')
    # DatetimeIndex(['1970-01-31',
    #                '1970-02-28',
    #                '1970-03-31',
    #                '1970-04-30',
    #                '1970-05-31',
    #                '1970-06-30'],
    #                dtype='datetime64[ns]', freq='M')

Every day
^^^^^^^^^
.. code-block:: python

    pd.date_range('1970-01-01', periods=6, freq='D')
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'],
    #                dtype='datetime64[ns]', freq='D')

Every hour
^^^^^^^^^^
* Works also with ISO time format ``1970-01-01T00:00:00``
* If time is not provided, it will start since midnight ``00:00:00``

.. code-block:: python

    pd.date_range('1970-01-01 00:00:00', periods=6, freq='H')
    # DatetimeIndex(['1970-01-01 00:00:00',
    #                '1970-01-01 01:00:00',
    #                '1970-01-01 02:00:00',
    #                '1970-01-01 03:00:00',
    #                '1970-01-01 04:00:00',
    #                '1970-01-01 05:00:00'],
    #                dtype='datetime64[ns]', freq='H')

Every minute
^^^^^^^^^^^^
* Works also with ISO time format ``1970-01-01T00:00:00``
* If time is not provided, it will start since midnight ``00:00:00``

.. code-block:: python

    pd.date_range('1970-01-01 00:00:00', periods=6, freq='T')
    # DatetimeIndex(['1970-01-01 00:00:00',
    #                '1970-01-01 00:01:00',
    #                '1970-01-01 00:02:00',
    #                '1970-01-01 00:03:00',
    #                '1970-01-01 00:04:00',
    #                '1970-01-01 00:05:00'],
    #                dtype='datetime64[ns]', freq='T')

Every second
^^^^^^^^^^^^
* Works also with ISO time format ``1970-01-01T00:00:00``
* If time is not provided, it will start since midnight ``00:00:00``

.. code-block:: python

    pd.date_range('1970-01-01 00:00:00', periods=6, freq='S')
    # DatetimeIndex(['1970-01-01 00:00:00',
    #                '1970-01-01 00:00:01',
    #                '1970-01-01 00:00:02',
    #                '1970-01-01 00:00:03',
    #                '1970-01-01 00:00:05',
    #                '1970-01-01 00:00:06'],
    #                dtype='datetime64[ns]', freq='T')


Slicing
=======

Slicing by index numbers
------------------------
.. code-block:: python

    values = np.random.randn(5)
    indexes = ['a', 'b', 'c', 'd', 'e']

    s = pd.Series(values, index=indexes)
    # a   -1.613898
    # b   -0.212740
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

.. code-block:: python

    s[1]
    # -0.2127402802139687

.. code-block:: python

    s[2:]
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

.. code-block:: python

    s[1:-2]
    # b   -0.212740
    # c   -0.895467
    # dtype: float64

Slicing by index names
----------------------
.. code-block:: python

    values = np.random.randn(5)
    indexes = ['a', 'b', 'c', 'd', 'e']

    s = pd.Series(values, index=indexes)
    # a   -1.613898
    # b   -0.212740
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

.. code-block:: python

    s['b']
    # -0.2127402802139687

.. code-block:: python

    s['c':]
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

.. code-block:: python

    s['b':'c']
    # b   -0.212740
    # c   -0.895467
    # dtype: float64

.. code-block:: python

    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    values = [1, 3, 5, np.nan, 6, 8]
    s = pd.Series(values, index=indexes)
    # 1970-01-01    1.0
    # 1970-01-02    3.0
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # 1970-01-06    8.0
    # Freq: D, dtype: float64

    s['1970-01-03':'1970-01-05']
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # Freq: D, dtype: float64

Substitute values
=================
.. code-block:: python

    values = [1, 3, 5, np.nan, 6, 8]
    s = pd.Series(values)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64

Fill ``NaN`` values
-------------------
* can use with ``inplace=True``

.. code-block:: python

    s.fillna(0.0)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    0.0
    # 4    6.0
    # 5    8.0
    # dtype: float64

Drop rows with ``NaN`` values
-----------------------------
.. code-block:: python

    s.dropna(inplace=True)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 4    6.0
    # 5    8.0
    # dtype: float64

Reset index
-----------
* ``drop=True`` to avoid the old index being added as a column

.. code-block:: python

    s.reset_index(drop=True)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    6.0
    # 4    8.0
    # dtype: float64


Arithmetic operations
=====================
.. code-block:: python

    values = np.random.randn(5)
    indexes = ['a', 'b', 'c', 'd', 'e']

    s = pd.Series(values, index=indexes)
    # a   -1.613898
    # b   -0.212740
    # c   -0.895467
    # d    0.386902
    # e   -0.510805
    # dtype: float64

Multiply by scalar
------------------
.. code-block:: python

    s * 5
    # a   -8.069489
    # b   -1.063701
    # c   -4.477333
    # d    1.934512
    # e   -2.554026
    # dtype: float64

Multiply by itself
------------------
.. code-block:: python

    s * s
    # a    2.604666
    # b    0.045258
    # c    0.801860
    # d    0.149694
    # e    0.260922
    # dtype: float64

.. code-block:: python

    s ** 3
    # a   -4.203665
    # b   -0.009628
    # c   -0.718039
    # d    0.057917
    # e   -0.133280
    # dtype: float64

Sum elements
------------
.. code-block:: python

    s.sum()
    # -2.846007328675207

.. code-block:: python

    sum(s)
    # -2.846007328675207

Add values
----------
* Uses inner join
* ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

.. code-block:: python

    import numpy as np

    a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
    # a    1.0
    # b    1.0
    # c    1.0
    # d    NaN
    # dtype: float64

    b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'x', 'y'])
    # a    1.0
    # b    NaN
    # x    1.0
    # y    NaN
    # dtype: float64

.. code-block:: python

    a + b
    # a    2.0
    # b    NaN
    # c    NaN
    # d    NaN
    # x    NaN
    # y    NaN
    # dtype: float64

.. code-block:: python

    # ``fill_value``: If data in both corresponding ``Series`` locations is missing the result will be missing

    a.add(b, fill_value=0)
    # a    2.0
    # b    1.0
    # c    1.0
    # d    NaN
    # x    1.0
    # y    NaN
    # dtype: float64


Assignments
===========

Even Numbers
------------
* Filename: ``pandas_even_numbers.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Stwórz ``pd.Series`` z 10 liczbami parzystymi
#. Podnieś wszystkie elementy do kwadratu
#. Dodaj 5 do każdego z elementów

Slicing
-------
* Filename: ``pandas_even_numbers.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min

#. Stwórz ``pd.Series`` z 26 losowymi liczbami całkowitymi z przedziału ``[10, 100)``
#. Nazwij indeksy jak kolejne litery alfabetu łacińskiego (bez polskich znaków)
#. Za pomocą funkcji ``median`` z biblioteki ``statistics`` znajdź medianę alfabetu
#. Jak znaleźć medianę dla parzystej długości listy? Użyj dolnego elementu.
#. Jak znaleźć element w liście o zadanym indeksie?
#. Wytnij z serii po 3 elementy w górę i w dół od wyszukanego środka
#. Zsumuj wyniki

:Hint:
    * ``import string``, ``string.ascii_lowercase``
    * ``statistics.median_high()``, ``statistics.median_low()``
    * ``list.index(element)``
