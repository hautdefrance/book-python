********************
Pandas ``DataFrame``
********************


* 2-dimensional object
* Each column ``Series`` and have name
* All columns has common indexes
* Operations can be executed on columns or rows


Creating ``DataFrame``
======================
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

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "1970-01-01", "0.131926", "-1.825204", "-1.909562", "1.274718"
    "1970-01-02", "0.084471", "-0.932586", "0.160637", "-0.275183"
    "1970-01-03", "-1.308835", "-0.285436", "-0.757591", "-0.042493"
    "1970-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "1970-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"
    "1970-01-06", "1.361922", "-0.827940", "0.400024", "0.047176"

.. code-block:: python

    df2 = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                         'D' : np.array([3] * 4, dtype='int32'),
                         'E' : pd.Categorical(["test", "train", "test", "train"]),
                         'F' : 'foo' })

.. csv-table:: DataFrame
    :header-rows: 1

    "", "A", "B", "C", "D", "E", "F"
    "0", "1.0", "2013-01-02", "1.0", "3", "test", "foo"
    "1", "1.0", "2013-01-02", "1.0", "3", "train", "foo"
    "2", "1.0", "2013-01-02", "1.0", "3", "test", "foo"
    "3", "1.0", "2013-01-02", "1.0", "3", "train", "foo"

.. code-block:: python

    df3 = pd.DataFrame([{'A': 1, 'B': 2}, {'C': 3}])

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C"
    "0", "1.0", "2.0", "NaN"
    "1", "NaN", "NaN", "3.0"


Slicing by index
================
.. code-block:: python

    df[1:3]
    #                    A         B         C         D
    # 1970-01-02  0.084471 -0.932586  0.160637 -0.275183
    # 1970-01-03 -1.308835 -0.285436 -0.757591 -0.042493


Slicing by columns
==================
.. code-block:: python

    df2 = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                         'D' : np.array([3] * 4, dtype='int32'),
                         'E' : pd.Categorical(["test", "train", "test", "train"]),
                         'F' : 'foo' })

.. code-block:: python

    df2.E
    # 0     test
    # 1    train
    # 2     test
    # 3    train
    # Name: E, dtype: category
    # Categories (2, object): [test, train]

.. code-block:: python

    df2['E']
    # 0     test
    # 1    train
    # 2     test
    # 3    train
    # Name: E, dtype: category
    # Categories (2, object): [test, train]


.. code-block:: python

    df['A']
    # 1970-01-01    0.131926
    # 1970-01-02    0.084471
    # 1970-01-03   -1.308835
    # 1970-01-04   -0.974425
    # 1970-01-05    0.589973
    # 1970-01-06    1.361922
    # Freq: D, Name: A, dtype: float64


.. code-block:: python

    df3[['A', 'B']]

.. csv-table::
    :header-rows: 1

    "", "A", "B"
    "0", "1.0", "2.0"
    "1", "NaN", "NaN"


Filtering results
=================
.. code-block:: python

    df[df.B > 0.5]

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "1970-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "1970-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"


Locating values
===============
* Zalecane jest używanie zoptymalizowanych funkcji Pandas
* ``iloc`` integer locate (bez where i innych bajerów)

.. warning:: Start and the stop are included (different than slices)!

.. code-block:: python

    values = [[1, 2], [4, 5], [7, 8]]
    indexes = ['cobra', 'viper', 'sidewinder']
    columns = ['max_speed', 'shield']

    df = pd.DataFrame(values, index=indexes, columns=columns)
    #             max_speed  shield
    # cobra               1       2
    # viper               4       5
    # sidewinder          7       8

Single label:

    .. code-block:: python

        # Note this returns the row as a Series

        df.loc['viper']
        # max_speed    4
        # shield       5
        # Name: viper, dtype: int64

List of labels:

    .. code-block:: python

        # Note using ``[[]]`` returns a DataFrame

        df.loc[['viper', 'sidewinder']]
        #             max_speed  shield
        # viper               4       5
        # sidewinder          7       8

Single label for row and column:

    .. code-block:: python

        df.loc['cobra', 'shield']
        # 2

Slice with labels for row and single label for column:

    .. code-block:: python

        # Note that both the start and stop of the slice are included

        df.loc['cobra':'viper', 'max_speed']
        # cobra    1
        # viper    4
        # Name: max_speed, dtype: int64

Boolean list with the same length as the row axis:

    .. code-block:: python

        df.loc[[False, False, True]]
        #             max_speed  shield
        # sidewinder          7       8

Conditional that returns a boolean Series:

    .. code-block:: python

        df.loc[df['shield'] > 6]
        #             max_speed  shield
        # sidewinder          7       8

Conditional that returns a boolean Series with column labels specified:

    .. code-block:: python

        df.loc[df['shield'] > 6, ['max_speed']]
        #             max_speed
        # sidewinder          7

Callable that returns a boolean Series:

    .. code-block:: python

        df.loc[lambda df: df['shield'] == 8]
        #             max_speed  shield
        # sidewinder          7       8

Set value for all items matching the list of labels:

    .. code-block:: python

        df.loc[['viper', 'sidewinder'], ['shield']] = 50
        #             max_speed  shield
        # cobra               1       2
        # viper               4      50
        # sidewinder          7      50

Set value for an entire row:

    .. code-block:: python

        df.loc['cobra'] = 10
        #             max_speed  shield
        # cobra              10      10
        # viper               4      50
        # sidewinder          7      50

Set value for an entire column:

    .. code-block:: python

        df.loc[:, 'max_speed'] = 30
        #             max_speed  shield
        # cobra              30      10
        # viper              30      50
        # sidewinder         30      50

Set value for rows matching callable condition:

    .. code-block:: python

        df.loc[df['shield'] > 35] = 0
        #             max_speed  shield
        # cobra              30      10
        # viper               0       0
        # sidewinder          0       0

Getting values on a DataFrame with an index that has integer labels:

    .. code-block:: python

        values = [[1, 2], [4, 5], [7, 8]]
        indexes = [7, 8, 9]
        columns = ['max_speed', 'shield']

        df = pd.DataFrame(values, index=indexes, columns=)
        #    max_speed  shield
        # 7          1       2
        # 8          4       5
        # 9          7       8

Slice with integer labels for rows:

    .. code-block:: python

        # Note that both the start and stop of the slice are included

        df.loc[7:9]
        #    max_speed  shield
        # 7          1       2
        # 8          4       5
        # 9          7       8


Accessing values
================
* Access a single value for a row/column pair by integer position
* Use iat if you only need to get or set a single value in a DataFrame or Series
* ``iat`` integer at (bez where i innych bajerów)

.. code-block:: python

    df = pd.DataFrame([[0, 2, 3],
                       [0, 4, 1],
                       [10, 20, 30]], columns=['A', 'B', 'C'])
    #     A   B   C
    # 0   0   2   3
    # 1   0   4   1
    # 2  10  20  30

Get value at specified row/column pair:

    .. code-block:: python

        df.iat[1, 2]
        # 1

Set value at specified row/column pair:

    .. code-block:: python

        df.iat[1, 2] = 10
        df.iat[1, 2]
        # 10

Get value within a series:

    .. code-block:: python

        df.loc[0].iat[1]
        # 2


Show ``DataFrame`` index
========================
.. code-block:: python

    df.index
    # DatetimeIndex(['1970-01-01', '1970-01-02', '1970-01-03', '1970-01-04', '1970-01-05', '1970-01-06'],
    #               dtype='datetime64[ns]', freq='D')


Show ``DataFrame`` columns
==========================
.. code-block:: python

    df.columns
    # Index(['A', 'B', 'C', 'D'], dtype='object')


First ``n`` records in ``DataFrame``
====================================
.. code-block:: python

    df.head(2)
    #                    A         B         C         D
    # 1970-01-01  0.131926 -1.825204 -1.909562  1.274718
    # 1970-01-02  0.084471 -0.932586  0.160637 -0.275183


Last ``n`` records in ``DataFrame``
===================================
.. code-block:: python

    df.tail(3)
    #                    A         B         C         D
    # 1970-01-04 -0.974425  1.327082 -0.435516  1.328745
    # 1970-01-05  0.589973  0.748417 -1.680741  0.510512
    # 1970-01-06  1.361922 -0.827940  0.400024  0.047176


Sorting
=======

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


Transpose ``DataFrame``
=======================
.. code-block:: python

    df.T
    df.transpose()

=== ========== =========== ========== ========== ========== ==========
    1970-01-01  1970-01-02 1970-01-03 1970-01-04 1970-01-05 1970-01-06
=== ========== =========== ========== ========== ========== ==========
A   0.131926    0.084471   -1.308835  -0.974425  0.589973   1.361922
B   -1.825204   932586     -0.285436  1.327082   0.748417   -0.827940
C   -1.909562   0.160637   -0.757591  -0.435516  -1.680741  0.400024
D   1.274718    -0.275183  -0.042493  1.328745   0.510512   0.047176
=== ========== =========== ========== ========== ========== ==========


Adding columns
==============
.. code-block:: python

    df3['Z'] = ['aa', 'bb']

=== === === === ==
    A   B   C   Z
=== === === === ==
0   1.0 2.0 NaN aa
1   NaN NaN 3.0 bb
=== === === === ==

Zmiana pojedynczej wartości może być również zrobiona przez przypisanie; używamy wtedy komend lokalizacyjnych, np:


Removing ``NaN`` values
=======================
.. code-block:: python

    df3 = pd.DataFrame([{'A': 1, 'B': 2}, {'B': 2, 'C': 3}])

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   NaN 2.0 3.0
=== === === ===

.. code-block:: python

    df3.dropna(how='all')

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   NaN 2.0 3.0
=== === === ===

.. code-block:: python

    df3.dropna(how='any')

=== === === ===
    A   B   C
=== === === ===

.. code-block:: python

    df3.dropna(how='any', axis=1)

=== ===
    B
=== ===
0   2.0
1   2.0
=== ===


Substituting ``NaN`` values
===========================
.. code-block:: python

    df3.fillna(0.0)

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   NaN 2.0 3.0
=== === === ===

.. code-block:: python

    values={'A': 5, 'B': 7, 'C': 9}
    df3.fillna(values)

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 9.0
1   5.0 2.0 3.0
=== === === ===

.. code-block:: python

    df3.fillna(method='ffill')

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 NaN
1   1.0 2.0 3.0
=== === === ===

.. code-block:: python

    df3.fillna(method='bfill')

=== === === ===
    A   B   C
=== === === ===
0   1.0 2.0 3.0
1   NaN 2.0 3.0
=== === === ===


Descriptive Statistics
======================
.. code-block:: python

    df.mean()
    df.describe()

======= =========== =========== =========== =========
        A           B           C           D
======= =========== =========== =========== =========
count   6.000000    6.000000    6.000000    6.000000
mean    -0.019161   -0.299278   -0.703791   0.473913
std     0.988715    1.162060    0.943273    0.690404
min     -1.308835   -1.825204   -1.909562   -0.275183
25%     -0.709701   -0.906424   -1.449953   -0.020076
50%     0.108199    -0.556688   -0.596554   0.278844
75%     0.475461    0.489954    0.011598    1.083666
max     1.361922    1.327082    0.400024    1.328745
======= =========== =========== =========== =========

Dodatkowo, można używać funkcji znanych z baz danych jak grupowanie czy złączenie (join):


Grouping
========
.. code-block:: python

    df2.groupby('E').size()
    df2.groupby('E').mean()


Joins
=====
.. code-block:: python

    df2.join(df3, how='left', rsuffix='_3')  # gdyby była kolizja nazw kolumn, to dodaj suffix '_3'
    df2.merge(df3)
    df2.merge(df3, how='outer')

.. code-block:: python

    # Odpowiednik:
    # df2.join(df3, how='left', rsuffix='_3')
    df2.merge(df3, right_index=True, left_index=True, how='left', suffixes=('', '_3'))

.. code-block:: python

    df2.append(df3)                     # jak robi appenda, to nie zmienia indeksów (uwaga na indeksy powtórzone)
    df2.append(df3, ignore_index=True)  # nowy dataframe będzie miał kolejne indeksy

.. code-block:: python

    # Przydatne przy łączeniu dataframe wczytanych z wielu plików
    pd.concat([df2, df3])
    pd.concat([df2, df3], ignore_index=True)
    pd.concat([df2, df3], join='inner')


Percentiles
===========
.. code-block:: python

    df.qualtile(0.33)
    df.qualtile(0.33, 0.1, 0.99)


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
