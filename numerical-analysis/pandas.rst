******
Pandas
******

.. todo:: convert tables to CSV


Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way toward this goal. Here are just a few of the things that pandas does well:

    - Easy handling of missing data (represented as NaN) in floating point as well as non-floating point data
    - Size mutability: columns can be inserted and deleted from DataFrame and higher dimensional objects
    - Automatic and explicit data alignment: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let Series, DataFrame, etc. automatically align the data for you in computations
    - Powerful, flexible group by functionality to perform split-apply-combine operations on data sets, for both aggregating and transforming data
    - Make it easy to convert ragged, differently-indexed data in other Python and NumPy data structures into DataFrame objects
    - Intelligent label-based slicing, fancy indexing, and subsetting of large data sets
    - Intuitive merging and joining data sets
    - Flexible reshaping and pivoting of data sets
    - Hierarchical labeling of axes (possible to have multiple labels per tick)
    - Robust IO tools for loading data from flat files (CSV and delimited), Excel files, databases, and saving/loading data from the ultrafast HDF5 format
    - Time series-specific functionality: date range generation and frequency conversion, moving window statistics, moving window linear regressions, date shifting and lagging, etc.

    * http://pandas.pydata.org/

* http://pandas.pydata.org/
* http://pandas.pydata.org/pandas-docs/stable/10min.html
* http://pandas.pydata.org/pandas-docs/stable/index.html
* https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf

Podstawowymi strukturami danych w Pandas jest Series (seria) i DataFrame (obiekt tabeli); zobacz dokumentacje po więcej informacji.

.. code-block:: python

    import pandas as pd
    import numpy as np

Series
======
Series jest to jednowymiarowa struktura danych podobna do ``ndarray``. Serię tworzymy za pomocą polecenia ``Series``; jako dane możemy przekazać wiele kolekcji:

.. code-block:: python

    my_list = [1,3,5,np.nan,6,8]

    pd.Series(my_list)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64

Series posiada indeks, który będzie stworzony automatycznie jeżeli nie został przekazany lub można go stworzyć:

.. code-block:: python

    daty = pd.date_range('20170101', periods=6)
    # DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04', '2017-01-05', '2017-01-06'],
    #               dtype='datetime64[ns]', freq='D')

    s = pd.Series(l, index=daty)
    # 2017-01-01    1.0
    # 2017-01-02    3.0
    # 2017-01-03    5.0
    # 2017-01-04    NaN
    # 2017-01-05    6.0
    # 2017-01-06    8.0
    # Freq: D, dtype: float64

Niemniej, może to być każda seria która jest przynajmniej tak długa jak dane:

.. code-block:: python

    s = pd.Series(np.random.randn(5), index=list('abcde'))
    # a    1.016521
    # b   -0.441865
    # c    0.519119
    # d    0.948774
    # e    0.207670
    # dtype: float64

Pobierać dane z Series możemy jak w Numpy:

.. code-block:: python

    s[1]
    # -0.4418648443118965

    s[2:]
    # c    0.519119
    # d    0.948774
    # e    0.207670
    # dtype: float64

    s[1:-2]
    # b   -0.441865
    # c    0.519119
    # dtype: float64

Możemy też robić to jak w słowniku (lub lepiej), jeżeli indeks na to pozwala:

.. code-block:: python

    s["b"]
    # -0.4418648443118965

    s["c":]
    # c    0.519119
    # d    0.948774
    # e    0.207670
    # dtype: float64

    s["b":"c"]
    # b   -0.441865
    # c    0.519119
    # dtype: float64

Można też wykonywać operacje na serii:

.. code-block:: python

    s * 5
    # a    5.082606
    # b   -2.209324
    # c    2.595593
    # d    4.743869
    # e    1.038348
    # dtype: float64

    s ** 3
    # a    1.050387
    # b   -0.086272
    # c    0.139894
    # d    0.854059
    # e    0.008956
    # dtype: float64

    s * s
    # a    1.033315
    # b    0.195245
    # c    0.269484
    # d    0.900172
    # e    0.043127
    # dtype: float64

    s + s
    # a    2.033042
    # b   -0.883730
    # c    1.038237
    # d    1.897547
    # e    0.415339
    # dtype: float64


DataFrame
=========
DataFrame to zbiór serii.

DataFrame jest obiektem dwuwymiarowym, który w obsłudze przypomina tabelę. Każda kolumna ma nazwę i jest serią danych (Series). Wszystkie kolumny mają wspólny indeks. Operacje można wykonywać na całych kolumnach lub wierszach. DataFrame tworzymy operacją ``DataFrame``:


.. code-block:: python

    df = pd.DataFrame(np.random.randn(6,4), index=daty, columns=list('ABCD'))

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "2017-01-01", "0.131926", "-1.825204", "-1.909562", "1.274718"
    "2017-01-02", "0.084471", "-0.932586", "0.160637", "-0.275183"
    "2017-01-03", "-1.308835", "-0.285436", "-0.757591", "-0.042493"
    "2017-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "2017-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"
    "2017-01-06", "1.361922", "-0.827940", "0.400024", "0.047176"

.. code-block:: python

    rows = 10
    cols = 16

    df = pd.DataFrame(
        index=range(rows),
        columns=range(cols))

.. code-block:: python

    df2 = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test", "train", "test", "train"]),
                         'F' : 'foo' })

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D", "E", "F"
    "0", "1.0", "2013-01-02", "1.0", "3", "test", "foo"
    "1", "1.0", "2013-01-02", "1.0", "3", "train", "foo
    "2", "1.0", "2013-01-02", "1.0", "3", "test", "foo
    "3", "1.0", "2013-01-02", "1.0", "3", "train", "foo

.. code-block:: python

    df2.E
    # 0     test
    # 1    train
    # 2     test
    # 3    train
    # Name: E, dtype: category
    # Categories (2, object): [test, train]

    df2['E']
    # 0     test
    # 1    train
    # 2     test
    # 3    train
    # Name: E, dtype: category
    # Categories (2, object): [test, train]

.. code-block:: python

    df3 = pd.DataFrame([{'A': 1, 'B': 2}, {'C': 3}])

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C"
    "0", "1.0", "2.0", "NaN"
    "1", "NaN", "NaN", "3.0"

Istnieje też wiele innych metod tworzenia i czytania DataFrame, które zostały opicane w dokumentacji.

Pobierać dane można jak w serii i innych kolekcjach Pythonowych:

.. code-block:: python

    df['A'] =
    # 2017-01-01    0.131926
    # 2017-01-02    0.084471
    # 2017-01-03   -1.308835
    # 2017-01-04   -0.974425
    # 2017-01-05    0.589973
    # 2017-01-06    1.361922
    # Freq: D, Name: A, dtype: float64

    df[1:3]
    #                    A         B         C         D
    # 2017-01-02  0.084471 -0.932586  0.160637 -0.275183
    # 2017-01-03 -1.308835 -0.285436 -0.757591 -0.042493

Niemniej zalecane jest używanie zoptymalizowanych funkcji Pandas:

.. code-block:: python

    df.loc[:,'A']
    # 2017-01-01    0.131926
    # 2017-01-02    0.084471
    # 2017-01-03   -1.308835
    # 2017-01-04   -0.974425
    # 2017-01-05    0.589973
    # 2017-01-06    1.361922
    # Freq: D, Name: A, dtype: float64

    df.loc[daty[0],'A']
    # 0.13192554022073613

    df.at[daty[0],'A']
    # 0.13192554022073613

    df.iloc[:,0]  # integer locate (bez where i innych bajerów)
    # 2017-01-01    0.131926
    # 2017-01-02    0.084471
    # 2017-01-03   -1.308835
    # 2017-01-04   -0.974425
    # 2017-01-05    0.589973
    # 2017-01-06    1.361922
    # Freq: D, Name: A, dtype: float64

    df.iloc[0,0]
    # 0.13192554022073613

    df.iat[0,0]
    # 0.13192554022073613

    df.ix[0,0] # Deprecated in favor of df.iloc and df.loc
    # 0.13192554022073613

.. code-block:: python

    df3[['A', 'B']]

.. csv-table::
    :header-rows: 1

    "", "A", "B"
    "0", "1.0", "2.0"
    "1", "NaN", "NaN"

Można też używać wyrażeń boolowskich do filtrowania wyników:

.. code-block:: python

    df[df.B > 0.5]

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "2017-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "2017-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"

Jest też dostęp do poszczególnych elementów takich jak:

.. code-block:: python

    print('Indeks:\n{}'.format())
    print('Kolumny:\n{}'.format())
    print('Początek:\n{}'.format())
    print('Koniec:\n{}'.format())

    df.index
    # DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04', '2017-01-05', '2017-01-06'],
    #               dtype='datetime64[ns]', freq='D')

    df.columns
    # Index(['A', 'B', 'C', 'D'], dtype='object')

    df.head(2)
    #                    A         B         C         D
    # 2017-01-01  0.131926 -1.825204 -1.909562  1.274718
    # 2017-01-02  0.084471 -0.932586  0.160637 -0.275183

    df.tail(3)
    #                    A         B         C         D
    # 2017-01-04 -0.974425  1.327082 -0.435516  1.328745
    # 2017-01-05  0.589973  0.748417 -1.680741  0.510512
    # 2017-01-06  1.361922 -0.827940  0.400024  0.047176

Dane można też sortować po indeksie:

.. code-block:: python

    df.sort_index(ascending=False) # default axis=0
    df.sort_index(ascending=False, inplace=True)

.. csv-table::
    :header-rows: 1

    "", "A", "B", "C", "D"
    "2017-01-06", "1.361922", "-0.827940", "0.400024", "0.047176"
    "2017-01-05", "0.589973", "0.748417", "-1.680741", "0.510512"
    "2017-01-04", "-0.974425", "1.327082", "-0.435516", "1.328745"
    "2017-01-03", "-1.308835", "-0.285436", "-0.757591", "-0.042493"
    "2017-01-02", "0.084471", "-0.932586", "0.160637", "-0.275183"
    "2017-01-01", "0.131926", "-1.825204", "-1.909562", "1.274718"

Po kolumnach:

.. code-block:: python

    df.sort_index(axis=1, ascending=False)

.. csv-table::
    :header-rows: 1

    "", "D", "C", "B", "A"
    "2017-01-01", "1.274718 ", "-1.909562", "-1.825204", "0.131926"
    "2017-01-02", "-0.275183", "0.160637", "-0.932586", "0.084471"
    "2017-01-03", "-0.042493", "-0.757591", "-0.285436", "-1.308835"
    "2017-01-04", "1.328745", "-0.435516", "1.327082", "-0.974425"
    "2017-01-05", "0.510512", "-1.680741", "0.748417", "0.589973"
    "2017-01-06", "0.047176", "0.400024", "-0.827940", "1.361922"

Lub po wartościach:

.. code-block:: python

    df.sort_values('B')
    df.sort_values('B', inplace=True)

    # można sortować po wielu kolumnach (jeżeli wartości w pierwszej będą równe)
    df.sort_values(['B', 'C'])
    df.sort_values(['B', 'C'])

=========== =========== =========== =========== =========
            A           B           C           D
=========== =========== =========== =========== =========
2017-01-01  0.131926    -1.825204   -1.909562   1.274718
2017-01-02  0.084471    -0.932586   0.160637    -0.275183
2017-01-06  1.361922    -0.827940   0.400024    0.047176
2017-01-03  -1.308835   -0.285436   -0.757591   -0.042493
2017-01-05  0.589973    0.748417    -1.680741   0.510512
2017-01-04  -0.974425   1.327082    -0.435516   1.328745
=========== =========== =========== =========== =========

Można też tabelę transponować:

.. code-block:: python

    df.T

=== ========== =========== ========== ========== ========== ==========
    2017-01-01  2017-01-02 2017-01-03 2017-01-04 2017-01-05 2017-01-06
=== ========== =========== ========== ========== ========== ==========
A   0.131926    0.084471   -1.308835  -0.974425  0.589973   1.361922
B   -1.825204   932586     -0.285436  1.327082   0.748417   -0.827940
C   -1.909562   0.160637   -0.757591  -0.435516  -1.680741  0.400024
D   1.274718    -0.275183  -0.042493  1.328745   0.510512   0.047176
=== ========== =========== ========== ========== ========== ==========

Nową kolumnę dodajemy przez przypisanie:

.. code-block:: python

    df3['Z'] = ['aa', 'bb']

=== === === === ==
    A   B   C   Z
=== === === === ==
0   1.0 2.0 NaN aa
1   NaN NaN 3.0 bb
=== === === === ==

Zmiana pojedynczej wartości może być również zrobiona przez przypisanie; używamy wtedy komend lokalizacyjnych, np:

Removing DataFrame None values
------------------------------
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
----------------------
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

.. code-block:: python

    df2.groupby('E').size()
    df2.groupby('E').mean()

.. code-block:: python

    df2.join(df3, how='left', rsuffix='_3')  # gdyby była kolizja nazw kolumn, to dodaj suffix '_3'
    df2.merge(df3)
    df2.merge(df3, how='outer')

.. code-block:: python

    # Odpowiednik:
    # df2.join(df3, how='left', rsuffix='_3')
    df2.merge(df3, right_index=True, left_index=True, how='left', suffixes=('', '_3'))

.. code-block:: python

    df2.append(df3)  # jak robi appenda, to nie zmienia indeksów (uwaga na indeksy powtórzone)
    df2.append(df3, ignore_index=True)  # nowy dataframe będzie miał kolejne indeksy

.. code-block:: python

    # Przydatne przy łączeniu dataframe wczytanych z wielu plików
    pd.concat([df2, df3])
    pd.concat([df2, df3], ignore_index=True)
    pd.concat([df2, df3], join='inner')


Percentiles
-----------
.. code-block:: python

    df.qualtile(0.33)
    df.qualtile(0.33, 0.1, 0.99)

Import
======
- ``pd.read_*``

.. code-block:: python

    pd.read_csv()
    pd.read_excel()
    pd.read_html()
    pd.read_json()
    pd.read_sas()
    pd.read_sql()
    pd.read_sql_query()
    pd.read_sql_table()

Export
======
- Dane, które są w dataFrame można wyeksportować
- ``df.to_*``

.. code-block:: python

    df.to_csv()
    df.to_excel()
    df.to_html()
    df.to_json()
    df.to_latex()
    df.to_dict()

Display Output
==============
.. code-block:: python

    # Set options for whole script
    pd.set_option('display.height',1000)
    pd.set_option('display.max_rows',500)
    pd.set_option('display.max_columns',500)
    pd.set_option('display.width',1000)

.. code-block:: python

    # Unlimited for whole script
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

.. code-block:: python

    # Use config only with context
    with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
        print(df)

Vizualization
=============

Hist
----
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    data.hist()
    plt.show()

.. figure:: img/matplotlib-pd-hist.png
    :scale: 100%
    :align: center

    Vizualization using hist

Density
-------
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
    plt.show()

.. figure:: img/matplotlib-pd-density.png
    :scale: 100%
    :align: center

    Vizualization using density

Box
---
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
    plt.show()

.. figure:: img/matplotlib-pd-box.png
    :scale: 100%
    :align: center

    Vizualization using density

Scatter matrix
--------------
* The in ``pandas`` version ``0.22`` plotting module has been moved from ``pandas.tools.plotting`` to ``pandas.plotting``
* As of version ``0.19``, the ``pandas.plotting`` library did not exist

.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd
    from pandas.plotting import scatter_matrix

    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/data-vizualization/data/iris.csv'
    data = pd.read_csv(url)

    scatter_matrix(data)
    plt.show()

.. figure:: img/matplotlib-pd-scatter-matrix.png
    :scale: 100%
    :align: center

    Vizualization using density


Practical Example
=================
.. code-block:: python

    import pandas
    from reach.importer.models import Spreadsheet

    data_frame = pandas.read_excel(
        io='filename.xls',
        encoding='utf-8',
        parse_dates=['from', 'to'],  # list of columns to parse for dates
        sheet_name=['Sheet 1'],
        skip_blank_lines=True,
        skiprows=1,
    )

    # Rename Columns to match database columns
    data_frame.rename(columns={
        'from': 'date_start',
        'to': 'date_end',
    }, inplace=True)

    # Drop all records where "Name" is empty (NaN)
    data_frame.dropna(subset=['name'], how='all', inplace=True)

    # choose columns
    columns = ['name', 'date_start', 'date_end']

    # Add metadata
    data_frame['blacklist'] = [True, False, True, False]
    columns = columns + ['blacklist']

    # Change NaN to None
    data_frame.fillna(None, inplace=True)

    return df[columns].to_dict('records')


Assignments
===========

Iris
----
* https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv

#. Mając dane Irysów przekonwertuj je na dataframe
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

Cars
----
Należy stworzyć DataFrame samochody z losową kolumną liczb całkowitych przebieg z przedziału [0, 200 000] oraz spalanie z przedziału [2, 20].

dodaj kolumnę marka:

- jeżeli samochód ma spalanie [0, 5] marka to VW
- jeżeli samochód ma spalanie [6, 10] marka to Ford
- jeżeli samochód ma spalanie 11 i więcej, marka to UAZ

dodaj kolumnę pochodzenie:

- jeżeli przebieg poniżej 100 km, pochodzenie nowy
- jeżeli przebieg powyżej 100 km, pochodzenie uzywany
- jeżeli przebieg powyżej 100 000 km, pochodzenie z niemiec

przeanalizuj dane statystycznie

:Zadanie z gwiazdką:
    #. pogrupuj dane po marce i po pochodzenie:

- sprawdź liczność grup
- wykonaj analizę statystyczną

.. code-block:: python

    np.random.randint()
    np.random.randn()  # rozklad normalny
    np.random.rand()

.. code-block:: python

    n = 50

    samochody = pd.DataFrame({
        'przebieg': np.random.randint(0, 200_000, size=n),
        'spalanie': 2 + 18*np.random.rand(n),
    })

    samochody.head()

=== ======== ===========
    przebieg spalanie
=== ======== ===========
0   5588     15.264853
1   99747    4.308231
2   97302    11.575376
3   117155   18.862744
4   73709    18.138283
=== ======== ===========

.. code-block:: python

    samochody.describe()

======= =============== ==========
        przebieg        spalanie
======= =============== ==========
count   0.000000        50.000000
mean    96794.320000    10.307848
std     62282.663803    5.036276
min     2143.000000     2.132470
25%     36741.500000    5.952677
50%     93007.000000    10.316452
75%     154008.500000   13.820076
max     198046.000000   19.694027
======= =============== ==========

.. code-block:: python

    samochody.loc[samochody.spalanie < 5, 'marka'] = 'VW'
    # alternatywnie
    samochody['marka'] = pd.cut(samochody.spalanie,
                            bins=[0, 5, 10, 100],
                            labels=['VW', 'Ford', 'UAZ'])

== ======== ========== =====
   przebieg spalanie
== ======== ========== =====
0  5588     15.264853  UAZ
1  99747    4.308231   VW
2  97302    11.575376  UAZ
3  117155   18.862744  UAZ
4  73709    18.138283  UAZ
== ======== ========== =====


.. code-block:: python

    samochody['pochodzenie'] = pd.cut(samochody.przebieg,
                                      bins=[0, 100, 1e5, np.inf],
                                      labels=['nowy', 'uzywany', 'z niemiec'])
    samochody.head()

=== ======== =========== ===== ===========
    przebieg spalanie    marka pochodzenie
=== ======== =========== ===== ===========
0   5588     15.264853   UAZ   uzywany
1   99747    4.308231    VW    uzywany
2   97302    11.575376   UAZ   uzywany
3   117155   18.862744   UAZ   z niemiec
4   73709    18.138283   UAZ   uzywany
=== ======== =========== ===== ===========

.. code-block:: python

    samochody.groupby(['marka', 'pochodzenie']).describe().T

=================== ========================== ========================== ==========================
        marka       VW                         Ford                       UAZ
        pochodzenie uzywany      z niemiec     uzywany      z niemiec     uzywany      z niemiec
=================== ========================== ========================== ==========================
przebieg    count   5.000000     7.000000      11.000000    6.000000      13.000000    8.000000
            mean    53130.600000 147559.285714 52263.909091 179048.000000 47688.615385 147846.375000
            std     43207.205363 27935.718079  35514.114012 8345.607132   33578.183062 29669.603213
            min     2988.000000  109498.000000 8550.000000  164217.000000 1746.000000  105497.000000
            25%     20030.000000 130846.000000 23674.000000 176727.500000 14940.000000 122390.750000
            50%     48931.000000 147778.000000 50347.000000 181309.500000 50751.000000 154775.500000
            75%     93957.000000 164885.000000 85860.500000 183584.500000 73709.000000 166537.500000
            max     99747.000000 184177.000000 99884.000000 187909.000000 97302.000000 192988.000000
spalanie    count    5.000000    7.000000      11.000000   6.000000       13.000000    8.000000
            mean     3.508948    3.645898      7.409556    7.028662       14.566981    16.438332
            std      1.068128    0.867709      1.636214    1.803311       3.030231     3.786771
            min      2.486142    2.426900      5.123669    5.076044       10.143688    10.215177
            25%      2.697416    3.021124      6.182025    5.648620       12.600224    15.449772
            50%      3.108775    3.870043      7.442336    6.652541       13.524153    17.990315
            75%      4.308231    4.245297      8.671341    8.621158       18.009058    18.933888
            max      4.944177    4.691502      9.611147    9.199502       19.708519    19.580096
=================== ========================== ========================== ==========================
