*****************
Pandas ``Series``
*****************


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
.. code-block:: python

    values = [1, 3, 5, np.nan, 6, 8]
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    s = pd.Series(values, index=indexes)
    # 1970-01-01    1.0
    # 1970-01-02    3.0
    # 1970-01-03    5.0
    # 1970-01-04    NaN
    # 1970-01-05    6.0
    # 1970-01-06    8.0
    # Freq: D, dtype: float64

.. code-block:: python

    values = np.random.randn(5)
    indexes = ['a', 'b', 'c', 'd', 'e']

    s = pd.Series(values, index=indexes)
    # a    1.016521
    # b   -0.441865
    # c    0.519119
    # d    0.948774
    # e    0.207670
    # dtype: float64


Slicing by index numbers
========================
.. code-block:: python

    s[1]
    # -0.4418648443118965

.. code-block:: python

    s[2:]
    # c    0.519119
    # d    0.948774
    # e    0.207670
    # dtype: float64

.. code-block:: python

    s[1:-2]
    # b   -0.441865
    # c    0.519119
    # dtype: float64


Slicing by index names
======================
.. code-block:: python

    s['b']
    # -0.4418648443118965

.. code-block:: python

    s['c':]
    # c    0.519119
    # d    0.948774
    # e    0.207670
    # dtype: float64

.. code-block:: python

    s['b':'c']
    # b   -0.441865
    # c    0.519119
    # dtype: float64


Arithmetic operations
=====================
.. code-block:: python

    s * 5
    # a    5.082606
    # b   -2.209324
    # c    2.595593
    # d    4.743869
    # e    1.038348
    # dtype: float64

.. code-block:: python

    s ** 3
    # a    1.050387
    # b   -0.086272
    # c    0.139894
    # d    0.854059
    # e    0.008956
    # dtype: float64

.. code-block:: python

    s * s
    # a    1.033315
    # b    0.195245
    # c    0.269484
    # d    0.900172
    # e    0.043127
    # dtype: float64

.. code-block:: python

    s + s
    # a    2.033042
    # b   -0.883730
    # c    1.038237
    # d    1.897547
    # e    0.415339
    # dtype: float64


Assignments
===========

Even Numbers
------------
#. Stwórz ``pd.Series`` z liczbami parzystymi
#. Podnieś wszystkie elementy do kwadratu
#. Dodaj 5 do każdego z elementów

:About:
    * Filename: ``pandas_even_numbers.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

Slicing
-------
#. Stwórz ``pd.Series`` z 24 losowymi liczbami z przedziału ``(10, 100]``
#. Nazwij kolumny jak kolejne litery alfabetu łacińskieego (bez polskich znaków)
#. Za pomocą funkcji statystycznych znajdź medianę alfabetu
#. Wytnij z serii po 3 elementy w prawo i w lewo od mediany

:About:
    * Filename: ``pandas_even_numbers.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min
