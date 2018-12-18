********************
Pandas ``DataFrame``
********************


* 2-dimensional object
* Each column ``Series`` and have name
* All columns has common indexes
* Operations can be executed on columns or rows


Creating
========

Simple ``pd.DataFrame``
-----------------------
.. code-block:: python

    values = np.arange(16).reshape(4, 4)
    indexes = range(4)
    columns = range(4)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #     0   1   2   3
    # 0   0   1   2   3
    # 1   4   5   6   7
    # 2   8   9  10  11
    # 3  12  13  14  15

With ``date`` indexes
---------------------
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

With custom values in columns
-----------------------------
.. code-block:: python

    df = pd.DataFrame({ 'A' : 1.,
                        'B' : pd.Timestamp('1961-04-12'),
                        'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D' : np.array([3] * 4, dtype='int32'),
                        'E' : pd.Categorical(["test", "train", "test", "train"]),
                        'F' : 'foo' })

.. csv-table:: DataFrame
    :header-rows: 1

    "", "A", "B", "C", "D", "E", "F"
    "0", "1.0", "1961-04-12", "1.0", "3", "test", "foo"
    "1", "1.0", "1961-04-12", "1.0", "3", "train", "foo"
    "2", "1.0", "1961-04-12", "1.0", "3", "test", "foo"
    "3", "1.0", "1961-04-12", "1.0", "3", "train", "foo"

With multiple rows
------------------
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'C': 3}])

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C"
    "0", "1.0", "2.0", "NaN"
    "1", "NaN", "NaN", "3.0"


Properties
==========
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

Indexes
-------
.. code-block:: python

    df.index
    # DatetimeIndex(['1970-01-01', '1970-01-02', '1970-01-03', '1970-01-04', '1970-01-05', '1970-01-06'],
    #               dtype='datetime64[ns]', freq='D')

Columns
-------
.. code-block:: python

    df.columns
    # Index(['Morning', 'Noon', 'Evening', 'Midnight'], dtype='object')


Slicing
=======

Slicing by index
----------------
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

.. code-block:: python

    df[1:3]
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749


Slicing by columns
------------------
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

.. code-block:: python

    df.Morning
    # 1970-01-01   -0.438232
    # 1970-01-02   -1.798254
    # 1970-01-03   -0.802938
    # 1970-01-04    0.820863
    # 1970-01-05    1.800466
    # 1970-01-06    0.141029
    # Freq: D, Name: Morning, dtype: float64

.. code-block:: python

    df['Morning']
    # 1970-01-01   -0.438232
    # 1970-01-02   -1.798254
    # 1970-01-03   -0.802938
    # 1970-01-04    0.820863
    # 1970-01-05    1.800466
    # 1970-01-06    0.141029
    # Freq: D, Name: Morning, dtype: float64

.. code-block:: python

    df[['Morning', 'Evening']]
    #               Morning    Evening
    # 1970-01-01  -0.438232  -1.113116
    # 1970-01-02  -1.798254  -0.946041
    # 1970-01-03  -0.802938  -0.258279
    # 1970-01-04   0.820863  -0.901532
    # 1970-01-05   1.800466   0.611194
    # 1970-01-06   0.141029  -0.046938


Filtering
=========
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

.. code-block:: python

    df[df['Morning'] < 0]
    #               Morning       Noon    Evening   Midnight
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875


Locating values
===============
* Zalecane jest używanie zoptymalizowanych funkcji Pandas
* ``iloc`` integer locate (bez where i innych bajerów)

.. warning::
    * Start and the stop are included.
    * This is different behavior than Python slices!

.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

Single label
------------
* Returns the row as a Series

.. code-block:: python

    df.loc['1970-01-01']
    # Morning    -0.438232
    # Noon        1.493865
    # Evening    -1.113116
    # Midnight   -0.042712
    # Name: 1970-01-01 00:00:00, dtype: float64

Range
-----
.. code-block:: python

    df.loc['1970-01-02': '1970-01-04']
    #               Morning       Noon    Evening   Midnight
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697

Single label for row and column
-------------------------------
.. code-block:: python

    df.loc['1970-01-02', 'Morning']
    # -1.7982538699804334

Slice with labels for row and single label for column
-----------------------------------------------------
* Note that both the start and stop of the slice are included

.. code-block:: python

    df.loc['1970-01-02': '1970-01-04', 'Noon']
    # 1970-01-02   -1.440613
    # 1970-01-03    0.301141
    # 1970-01-04   -0.574301
    # Freq: D, Name: Noon, dtype: float64

Boolean list with the same length as the row axis
-------------------------------------------------
* Print row for given index is ``True``
* Default to ``False``

.. code-block:: python

    df.loc[[True, False, True]]
    #               Morning      Noon    Evening   Midnight
    # 1970-01-01  -0.438232  1.493865  -1.113116  -0.042712
    # 1970-01-03  -0.802938  0.301141  -0.258279  -1.492688

Conditional that returns a boolean Series
-----------------------------------------
.. code-block:: python

    df.loc[df['Morning'] < 0]
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865  -1.113116  -0.042712
    # 1970-01-02  -1.798254  -1.440613  -0.946041  -2.732719
    # 1970-01-03  -0.802938   0.301141  -0.258279  -1.492688

Conditional that returns a boolean Series with column labels specified
----------------------------------------------------------------------
.. code-block:: python

    df.loc[df['Morning'] < 0, 'Evening']
    # 1970-01-01   -1.113116
    # 1970-01-02   -0.946041
    # 1970-01-03   -0.258279
    # Freq: D, Name: Evening, dtype: float64

.. code-block:: python

    df.loc[df['Morning'] < 0, ['Morning', 'Evening']]
    #               Morning    Evening
    # 1970-01-01  -0.438232  -1.113116
    # 1970-01-02  -1.798254  -0.946041
    # 1970-01-03  -0.802938  -0.258279

Filtering with callable
-----------------------
.. code-block:: python

    def morning_below_zero(df):
        return df['Morning'] < 0

    df.loc[morning_below_zero]
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865  -1.113116  -0.042712
    # 1970-01-02  -1.798254  -1.440613  -0.946041  -2.732719
    # 1970-01-03  -0.802938   0.301141  -0.258279  -1.492688

.. code-block:: python

    df.loc[lambda df: df['Morning'] < 0]
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865  -1.113116  -0.042712
    # 1970-01-02  -1.798254  -1.440613  -0.946041  -2.732719
    # 1970-01-03  -0.802938   0.301141  -0.258279  -1.492688

Set value for all items matching the list of labels
---------------------------------------------------
.. code-block:: python

    df.loc[df['Morning'] < 0, 'Evening'] = 0.0
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865   0.000000  -0.042712
    # 1970-01-02  -1.798254  -1.440613   0.000000  -2.732719
    # 1970-01-03  -0.802938   0.301141   0.000000  -1.492688
    # 1970-01-04   0.820863  -0.574301  -0.901532  -0.191122
    # 1970-01-05   1.800466  -0.777165   0.611194   1.345492
    # 1970-01-06   0.141029  -0.134463  -0.046938   0.401554

Set value for an entire row
---------------------------
.. code-block:: python

    df.loc['1970-01-01'] = 0.0
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.000000   0.000000   0.000000   0.000000
    # 1970-01-02   0.391381  -0.034658  -0.026441  -0.528525
    # 1970-01-03   0.292151   1.328559   1.510460   0.973299
    # 1970-01-04   0.985247   1.033980  -0.688412   1.171957
    # 1970-01-05  -0.210144   0.112805  -0.691808   0.339706
    # 1970-01-06   1.259968  -0.283706  -1.333459  -0.962464

Set value for an entire column
------------------------------
.. code-block:: python

    df.loc[:, 'Evening'] = 0.0
    #               Morning       Noon  Evening   Midnight
    # 1970-01-01   0.000000   0.000000      0.0   0.000000
    # 1970-01-02   0.391381  -0.034658      0.0  -0.528525
    # 1970-01-03   0.292151   1.328559      0.0   0.973299
    # 1970-01-04   0.985247   1.033980      0.0   1.171957
    # 1970-01-05  -0.210144   0.112805      0.0   0.339706
    # 1970-01-06   1.259968  -0.283706      0.0  -0.962464

Set value for rows matching callable condition
----------------------------------------------
* Important!

.. code-block:: python

    df.loc[df['Morning'] < 0] = 0.0
    #              Morning       Noon  Evening   Midnight
    # 1970-01-01  0.000000   0.000000      0.0   0.000000
    # 1970-01-02  0.391381  -0.034658      0.0  -0.528525
    # 1970-01-03  0.292151   1.328559      0.0   0.973299
    # 1970-01-04  0.985247   1.033980      0.0   1.171957
    # 1970-01-05  0.000000   0.000000      0.0   0.000000
    # 1970-01-06  1.259968  -0.283706      0.0  -0.962464


Accessing values
================
* Access a single value for a row/column pair by integer position
* Use iat if you only need to get or set a single value in a DataFrame or Series
* ``iat`` integer at (bez where i innych bajerów)

.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

Get value at specified row/column pair
--------------------------------------
* First argument is column
* Second argument is row

.. code-block:: python

    df.iat[0, 0]
    # -0.728881431659923

    df.iat[1, 0]
    # 1.2427906060319527

    df.iat[0, 1]
    # 2.4525672341751084

Set value at specified row/column pair
--------------------------------------
.. code-block:: python

    df.iat[0, 0] = 0.0
    df.iat[0, 0]
    # 0.0

Get value within a series
-------------------------
* ``loc`` returns Series

.. code-block:: python

    df.loc['1970-01-01'].iat[1]
    # 2.4525672341751084


Modifying values
================
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'C': 3}])

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C"
    "0", "1.0", "2.0", "NaN"
    "1", "NaN", "NaN", "3.0"

Adding column
-------------
.. code-block:: python

    df['Z'] = ['aa', 'bb']

=== === === === ==
    A   B   C   Z
=== === === === ==
0   1.0 2.0 NaN aa
1   NaN NaN 3.0 bb
=== === === === ==

Drop row if all values are ``NaN``
----------------------------------
* ``axis=0``: rows

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='all')
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

Drop column if all values are ``NaN``
-------------------------------------
* ``axis=1``: columns

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='all', axis=1)
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

Drop row if any value is ``NaN``
--------------------------------
* ``axis=0``: rows

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='any')
    #       A     B     C

Drop column if any value is ``NaN``
-----------------------------------
* ``axis=1``: columns

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.dropna(how='any', axis=1)
    #       B
    # 0   2.0
    # 1   2.0

Fill ``NA``/``NaN`` with specified values
-----------------------------------------
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.fillna(0.0)
    #       A     B     C
    # 0   1.0   2.0   0.0
    # 1   0.0   2.0   3.0

Fill ``NA``/``NaN`` with values from dict with column names
-----------------------------------------------------------
.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    values = {'A': 5, 'B': 7, 'C': 9}

    df.fillna(values)
    #       A     B     C
    # 0   1.0   2.0   9.0
    # 1   5.0   2.0   3.0

Fill ``NA``/``NaN`` values from previous row
--------------------------------------------
* ``ffill``: propagate last valid observation forward to next valid backfill

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.fillna(method='ffill')
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   1.0   2.0   3.0

Fill ``NA``/``NaN`` values from next row
----------------------------------------
* ``bfill``: use NEXT valid observation to fill gap

.. code-block:: python

    df = pd.DataFrame([ {'A': 1, 'B': 2},
                        {'B': 2, 'C': 3}])
    #       A     B     C
    # 0   1.0   2.0   NaN
    # 1   NaN   2.0   3.0

.. code-block:: python

    df.fillna(method='bfill')
    #       A     B     C
    # 0   1.0   2.0   3.0
    # 1   NaN   2.0   3.0

Transpose
---------
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    indexes = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

.. code-block:: python

    df.T
    df.transpose()
    #          1970-01-01  1970-01-02  1970-01-03  1970-01-04  1970-01-05  1970-01-06
    # Morning   -0.728881    1.242791   -0.300652    0.973488    0.527855    0.805407
    # Noon       2.452567    0.595302   -0.272770   -2.083819   -0.911698   -0.931830
    # Evening    0.911723    0.176457   -0.471503    0.402725   -0.842518   -0.063189
    # Midnight  -0.849580   -0.560606   -0.852577   -0.331235    1.653468   -0.792088

Substitute values in columns
----------------------------
.. code-block:: python

    df.loc[df['Species'] == 0, 'Species'] = 'Setosa'
    df.loc[df['Species'] == 1, 'Species'] = 'Versicolor'
    df.loc[df['Species'] == 2, 'Species'] = 'Virginica'

.. code-block:: python

    df['Species'].replace(to_replace={
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)


Selecting values
================
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

First ``n`` records
-------------------
.. code-block:: python

    df.head(2)
    #                    A          B          C          D
    # 1970-01-01  0.131926  -1.825204  -1.909562   1.274718
    # 1970-01-02  0.084471  -0.932586   0.160637  -0.275183

Last ``n`` records
------------------
.. code-block:: python

    df.tail(3)
    #                     A          B          C         D
    # 1970-01-04  -0.974425   1.327082  -0.435516  1.328745
    # 1970-01-05   0.589973   0.748417  -1.680741  0.510512
    # 1970-01-06   1.361922  -0.827940   0.400024  0.047176

Sample ``n`` elements
---------------------
.. code-block:: python

    df.sample()
    #                     A          B          C         D
    # 1970-01-05   0.589973   0.748417  -1.680741  0.510512

.. code-block:: python

    df.sample(2)
    #                     A          B          C         D
    # 1970-01-04  -0.974425   1.327082  -0.435516  1.328745
    # 1970-01-01  0.131926  -1.825204  -1.909562   1.274718

.. code-block:: python

    df.sample(n=2, repeat=True)
    #                     A          B          C         D
    # 1970-01-05   0.589973   0.748417  -1.680741  0.510512
    # 1970-01-05   0.589973   0.748417  -1.680741  0.510512

Sample ``n`` percent of elements
--------------------------------
* 0.05 is 5%
* 1.0 is 100%

.. code-block:: python

    df.sample(frac=0.05)
    #      Sepal length  Sepal width  Petal length  Petal width     Species
    # 146           5.9          3.0           4.2          1.5  Versicolor
    # 135           4.7          3.2           1.3          0.2      Setosa
    # 15            6.6          3.0           4.4          1.4  Versicolor
    # 68            5.0          3.6           1.4          0.2      Setosa
    # 42            6.2          2.8           4.8          1.8   Virginica
    # 10            6.5          3.0           5.2          2.0   Virginica
    # 17            5.8          2.7           5.1          1.9   Virginica
    # 66            5.4          3.4           1.7          0.2      Setosa


.. code-block:: python

    df.sample(frac=0.05).reset_index(drop=True)
    #      Sepal length  Sepal width  Petal length  Petal width     Species
    # 0             5.9          3.0           4.2          1.5  Versicolor
    # 1             4.7          3.2           1.3          0.2      Setosa
    # 2             6.6          3.0           4.4          1.4  Versicolor
    # 3             5.0          3.6           1.4          0.2      Setosa
    # 4             6.2          2.8           4.8          1.8   Virginica
    # 5             6.5          3.0           5.2          2.0   Virginica
    # 6             5.8          2.7           5.1          1.9   Virginica
    # 7             5.4          3.4           1.7          0.2      Setosa


Sorting
=======
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

Sort by index
-------------
.. code-block:: python

    df.sort_index(ascending=False) # default axis=0
    df.sort_index(ascending=False, inplace=True)

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "1970-01-06", "1.361922", "-0.827940", "0.400024", "0.047176"
    "1970-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"
    "1970-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "1970-01-03", "-1.308835", "-0.285436", "-0.757591", "-0.042493"
    "1970-01-02", "0.084471", "-0.932586", "0.160637", "-0.275183"
    "1970-01-01", "0.131926", "-1.825204", "-1.909562", "1.274718"

Sort by columns
---------------
.. code-block:: python

    df.sort_index(axis=1, ascending=False)

.. csv-table::
    :header-rows: 1

    "", "D", "C", "B", "A"
    "1970-01-01", "1.274718 ", "-1.909562", "-1.825204", "0.131926"
    "1970-01-02", "-0.275183", "0.160637", "-0.932586", "0.084471"
    "1970-01-03", "-0.042493", "-0.757591", "-0.285436", "-1.308835"
    "1970-01-04", "1.328745", "-0.435516", "1.327082", "-0.974425"
    "1970-01-05", "0.510512", "-1.680741", "0.748417", "0.589973"
    "1970-01-06", "0.047176", "0.400024", "-0.827940", "1.361922"

Sort by values
--------------
.. code-block:: python

    df.sort_values('B')
    df.sort_values('B', inplace=True)

    # można sortować po wielu kolumnach (jeżeli wartości w pierwszej będą równe)
    df.sort_values(['B', 'C'])
    df.sort_values(['B', 'C'])

=========== =========== =========== =========== =========
            A           B           C           D
=========== =========== =========== =========== =========
1970-01-01  0.131926    -1.825204   -1.909562   1.274718
1970-01-02  0.084471    -0.932586   0.160637    -0.275183
1970-01-06  1.361922    -0.827940   0.400024    0.047176
1970-01-03  -1.308835   -0.285436   -0.757591   -0.042493
1970-01-05  0.589973    0.748417    -1.680741   0.510512
1970-01-04  -0.974425   1.327082    -0.435516   1.328745
=========== =========== =========== =========== =========


Statistics
==========
.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

Arithmetic mean
---------------
.. code-block:: python

    df.mean()
    # A   -0.078742
    # B    0.241929
    # C    0.110231
    # D   -0.092946
    # dtype: float64

Descriptive stats
-----------------
.. code-block:: python

    df.describe()
    #               A          B          C          D
    # count  6.000000   6.000000   6.000000   6.000000
    # mean  -0.078742   0.241929   0.110231  -0.092946
    # std    0.690269   0.845521   0.746167   1.207483
    # min   -0.928127  -0.931601  -0.812575  -1.789321
    # 25%   -0.442016  -0.275899  -0.359650  -0.638282
    # 50%   -0.202288   0.287667  -0.045933  -0.332729
    # 75%    0.189195   0.882916   0.733453   0.902115
    # max    1.062487   1.190259   1.036800   1.323504

Percentiles
-----------
.. code-block:: python

    values = np.array([[1, 1], [2, 10], [3, 100], [4, 100]])
    columns = ['a', 'b']

    df = pd.DataFrame(values, columns=columns)
    #    a    b
    # 0  1    1
    # 1  2   10
    # 2  3  100
    # 3  4  100

.. code-block:: python

    df.quantile(.1)
    # a    1.3
    # b    3.7
    # dtype: float64

.. code-block:: python

    df.quantile([.1, .5])
    #        a     b
    # 0.1  1.3   3.7
    # 0.5  2.5  55.0

Other methods
-------------
.. csv-table:: Descriptive statistics
    :header-rows: 1

    "Function", "Description"
    "``count``", "Number of non-null observations"
    "``sum``", "Sum of values"
    "``mean``", "Mean of values"
    "``mad``", "Mean absolute deviation"
    "``median``", "Arithmetic median of values"
    "``min``", "Minimum"
    "``max``", "Maximum"
    "``mode``", "Mode"
    "``abs``", "Absolute Value"
    "``prod``", "Product of values"
    "``std``", "Unbiased standard deviation"
    "``var``", "Unbiased variance"
    "``sem``", "Unbiased standard error of the mean"
    "``skew``", "Unbiased skewness (3rd moment)"
    "``kurt``", "Unbiased kurtosis (4th moment)"
    "``quantile``", "Sample quantile (value at %)"
    "``cumsum``", "Cumulative sum"
    "``cumprod``", "Cumulative product"
    "``cummax``", "Cumulative maximum"
    "``cummin``", "Cumulative minimum"


Grouping
========
* Group series using mapper (dict or key function, apply given function to group, return result as series) or by a series of columns
* Check:

    - ``.value_counts()``
    - ``.nunique()``
    - ``.sum()``
    - ``.count()``
    - ``.max()``
    - ``.first()``

.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df = pd.DataFrame(values, index=indexes, columns=columns)

By count of elements
--------------------
.. code-block:: python

    df.groupby('D').size()
    #         D
    # -1.789321    1
    # -0.709686    1
    # -0.424071    1
    # -0.241387    1
    #  1.283282    1
    #  1.323504    1
    # dtype: int64

By mean of elements
-------------------
.. code-block:: python

    df.groupby('D').mean()
    #         D          A          B          C
    # -1.789321   0.257330   1.190259   0.074459
    # -0.709686  -0.459565   0.827296   0.953118
    # -0.424071   1.062487  -0.251961  -0.424092
    # -0.241387  -0.928127  -0.931601   1.036800
    # 1.283282   -0.015208   0.901456  -0.812575
    # 1.323504   -0.389369  -0.283878  -0.166324

Example
-------
.. code-block:: python

    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C' : np.random.randn(8),
                       'D' : np.random.randn(8)})

    #      A      B          C          D
    # 0  foo    one   0.239653  -1.505271
    # 1  bar    one   0.567327  -0.109503
    # 2  foo    two   1.726200  -0.401514
    # 3  bar  three  -1.145225   1.379611
    # 4  foo    two  -0.808037   1.148953
    # 5  bar    two   0.883013  -0.347327
    # 6  foo    one   0.225142  -0.995694
    # 7  foo  three  -0.484968  -0.547152

    df.groupby('A').mean()
    #   A         C          D
    # bar  0.101705   0.307594
    # foo  0.179598  -0.460136


Aggregations
============
* ``df.groupby('month', as_index=False).agg({"duration": "sum"})``

.. code-block:: python

    aggregations = {
        'duration':'sum',
        'date': lambda x: max(x) - 1
    }
    data.groupby('month').agg(aggregations)

.. code-block:: python

    aggregations = {
        'duration': [min, max, sum],        # find the min, max, and sum of the duration column
        'network_type': 'count',            # find the number of network type entries
        'date': [min, 'first', 'nunique']   # get the min, first, and number of unique dates per group
    }

    data.groupby(['month', 'item']).agg(aggregations)


Joins
=====

.. figure:: img/sql-joins.png
    :scale: 50%
    :align: center

    Joins

.. code-block:: python

    values = np.random.randn(6, 4)
    columns = ['A', 'B', 'C', 'D']
    indexes = pd.date_range('1970-01-01', periods=6)
    # DatetimeIndex(['1970-01-01',
    #                '1970-01-02',
    #                '1970-01-03',
    #                '1970-01-04',
    #                '1970-01-05',
    #                '1970-01-06'], dtype='datetime64[ns]', freq='D')

    df1 = pd.DataFrame(values, index=indexes, columns=columns)
    df2 = pd.DataFrame([ {'A': 1, 'B': 2},
                         {'C': 3}])

Left Join
---------
.. code-block:: python

    df1.join(df2, how='left', rsuffix='_2')  # gdyby była kolizja nazw kolumn, to dodaj suffix '_2'

.. code-block:: python

    df1.merge(df2, right_index=True, left_index=True, how='left', suffixes=('', '_2'))

Outer Join
----------
.. code-block:: python

    df1.merge(df2)
    df1.merge(df2, how='outer')

Append
------
* jak robi appenda, to nie zmienia indeksów (uwaga na indeksy powtórzone)
* nowy dataframe będzie miał kolejne indeksy

.. code-block:: python

    df1.append(df2)
    df1.append(df2, ignore_index=True)

Concat
------
* Przydatne przy łączeniu dataframe wczytanych z wielu plików

.. code-block:: python

    pd.concat([df1, df2])
    pd.concat([df1, df2], ignore_index=True)
    pd.concat([df1, df2], join='inner')


Practical Example
=================
.. code-block:: python

    import pandas as pd
    from reach.importer.models import Spreadsheet


    df = pd.read_excel(
        io='filename.xls',
        encoding='utf-8',
        parse_dates=['from', 'to'],  # list of columns to parse for dates
        sheet_name=['Sheet 1'],
        skip_blank_lines=True,
        skiprows=1,
    )

    # Rename Columns to match database columns
    df.rename(columns={
        'from': 'date_start',
        'to': 'date_end',
    }, inplace=True)

    # Drop all records where "Name" is empty (NaN)
    df.dropna(subset=['name'], how='all', inplace=True)

    # Add column ``blacklis`` with data
    df['blacklist'] = [True, False, True, False]

    # Change NaN to None
    df.fillna(None, inplace=True)

    # Choose columns
    columns = ['name', 'date_start', 'date_end', 'blacklist']

    return df[columns].to_dict('records')


Assignments
===========

Iris Dirty
----------
* https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-dirty.csv

#. Mając dane Irysów przekonwertuj je na ``DataFrame``
#. Pomiń pierwszą linię z metadanymi
#. Zmień nazwy kolumn na:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Podmień wartości w kolumnie species

    - 0 -> 'setosa',
    - 1 -> 'versicolor',
    - 2 -> 'virginica'

#. Ustaw wszystkiw wiersze w losowej kolejności i zresetuj index
#. Wyświetl pierwsze 5 i ostatnie 3 wiersze
#. Wykreśl podstawowe statystyki opisowe

:About:
    * Filename: ``pandas_iris_dirty.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min

Iris Clean
----------
* https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-clean.csv

#. Mając dane Irysów przekonwertuj je na ``DataFrame``
#. Podaj jawnie ``encoding``
#. Pierwsza linijka stanowi metadane (nie wyświetlaj jej)
#. Nazwy poszczególnych kolumn:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Przefiltruj ``inplace`` kolumnę 'Petal length' i pozostaw wartości powyżej 2.0
#. Dodaj kolumnę ``datetime`` i wpisz do niej dzisiejszą datę (UTC)
#. Dodaj kolumnę ``big_enough`` i dla wartości 'Petal width' powyżej 1.0 ustawi ``True``, a dla mniejszych ``False``
#. Pozostaw tylko kolumny 'Sepal length', 'Sepal width' oraz 'Species'
#. Wykreśl podstawowe statystyki opisowe

:About:
    * Filename: ``pandas_iris_clean.py``
    * Lines of code to write: 25 lines
    * Estimated time of completion: 25 min

Cars
----
#. Stwórz ``DataFrame`` samochody z:

    - losową kolumną liczb całkowitych przebieg z przedziału [0, 200 000]
    - losową kolumną spalanie z przedziału [2, 20]

#. Dodaj kolumnę marka:

    - jeżeli samochód ma spalanie [0, 5] marka to VW
    - jeżeli samochód ma spalanie [6, 10] marka to Ford
    - jeżeli samochód ma spalanie 11 i więcej, marka to UAZ

#. Dodaj kolumnę pochodzenie:

    - jeżeli przebieg poniżej 100 km, pochodzenie nowy
    - jeżeli przebieg powyżej 100 km, pochodzenie uzywany
    - jeżeli przebieg powyżej 100 000 km, pochodzenie z niemiec

#. Przeanalizuj dane statystycznie

    - sprawdź liczność grup
    - wykonaj analizę statystyczną

#. Pogrupuj dane po marce i po pochodzenie

:About:
    * Filename: ``pandas_cars.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 45 min

EVA
---
#. Na podstawie podanych URL:

    * https://www.worldspaceflight.com/bios/eva/eva.php
    * https://www.worldspaceflight.com/bios/eva/eva2.php
    * https://www.worldspaceflight.com/bios/eva/eva3.php
    * https://www.worldspaceflight.com/bios/eva/eva4.php

#. Scrappuj stronę wykorzystując ``pandas.read_html()``
#. Połącz dane wykorzystując ``pd.concat``
#. Przygotuj plik ``CSV`` z danymi dotyczącymi spacerów kosmicznych

:About:
    * Filename: ``pandas_eva.py``
    * Lines of code to write: 25 lines
    * Estimated time of completion: 30 min
