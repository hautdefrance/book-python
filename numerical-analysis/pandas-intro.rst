*******************
Pandas Introduction
*******************

.. todo:: convert tables to CSV
.. todo:: https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/


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


TL;DR
=====
.. csv-table:: Pandas most commonly used functions
    :header-rows: 1

    "Method", "Description"
    "``DataFrame.at()``", "Access a single value for a row/column label pair"
    "``DataFrame.iat()``", "Access a single value for a row/column pair by integer position"
    "``DataFrame.loc()``", "Access a group of rows and columns by label(s)"
    "``DataFrame.iloc()``", "Access a group of rows and columns by integer position(s)"


Import and Export
=================

Import data to ``DataFrame``
----------------------------
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    pd.read_csv()
    pd.read_excel()
    pd.read_html()
    pd.read_json()
    pd.read_sas()
    pd.read_sql()        # Read SQL query or database table into a DataFrame
    pd.read_sql_query()  # Read SQL query into a DataFrame
    pd.read_sql_table()  # Read SQL database table into a DataFrame


Export ``DataFrame``
--------------------
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    DataFrame.to_csv()
    DataFrame.to_excel()
    DataFrame.to_html()
    DataFrame.to_json()
    DataFrame.to_latex()
    DataFrame.to_dict()
    DataFrame.to_sql()


Workflow
========

Import
------
.. code-block:: python

    import pandas as pd

Set Variables
-------------
.. code-block:: python

    url = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'
    columns = [
        'Sepal length',
        'Sepal width',
        'Petal length',
        'Petal width',
        'Species'
    ]

Read data
---------
.. code-block:: python

    df = pd.read_csv(url, skiprows=1, names=columns)

First ``n`` records
-------------------
.. code-block:: python

    df.head(5)
    #   Sepal length  Sepal width  Petal length  Petal width  Species
    # 0           5.1          3.5           1.4          0.2        0
    # 1           4.9          3.0           1.4          0.2        0
    # 2           4.7          3.2           1.3          0.2        0
    # 3           4.6          3.1           1.5          0.2        0
    # 4           5.0          3.6           1.4          0.2        0

Last ``n`` records
------------------
.. code-block:: python

    df.tail(3)
    #      Sepal length  Sepal width  Petal length  Petal width  Species
    # 147           6.5          3.0           5.2          2.0        2
    # 148           6.2          3.4           5.4          2.3        2
    # 149           5.9          3.0           5.1          1.8        2

Change column Species values
----------------------------
.. code-block:: python

    df.Species.replace(to_replace={
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }, inplace=True)

Shuffle columns and reset indexes
---------------------------------
.. code-block:: python

    df = df.sample(frac=1.0).reset_index(drop=True)
    #      Sepal length  Sepal width     ...      Petal width     Species
    # 0             5.0          2.0     ...              1.0  versicolor
    # 1             6.4          2.7     ...              1.9   virginica
    # 2             5.6          3.0     ...              1.5  versicolor
    # 3             5.7          2.6     ...              1.0  versicolor
    # 4             6.4          3.1     ...              1.8   virginica
    # 5             4.6          3.6     ...              0.2      setosa
    # 6             5.9          3.0     ...              1.5  versicolor

Descriptive Statistics
----------------------
.. code-block:: python

    df.describe()
    #        Sepal length  Sepal width  Petal length  Petal width
    # count    150.000000   150.000000    150.000000   150.000000
    # mean       5.843333     3.057333      3.758000     1.199333
    # std        0.828066     0.435866      1.765298     0.762238
    # min        4.300000     2.000000      1.000000     0.100000
    # 25%        5.100000     2.800000      1.600000     0.300000
    # 50%        5.800000     3.000000      4.350000     1.300000
    # 75%        6.400000     3.300000      5.100000     1.800000
    # max        7.900000     4.400000      6.900000     2.500000


Display Output
==============
* Set options for whole script:

    .. code-block:: python

        pd.set_option('display.height',1000)
        pd.set_option('display.max_rows',500)
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width',1000)

* Unlimited for whole script:

    .. code-block:: python

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

* Use config only with context:

    .. code-block:: python

        with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
            print(df)


Vizualization
=============

Hist
----
.. code-block:: python

    import matplotlib.pyplot as plt
    import pandas as pd


    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-clean.csv'
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


    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-clean.csv'
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


    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-clean.csv'
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


    url = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-clean.csv'
    data = pd.read_csv(url)

    scatter_matrix(data)
    plt.show()

.. figure:: img/matplotlib-pd-scatter-matrix.png
    :scale: 100%
    :align: center

    Vizualization using density


Descriptive statistics
======================
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


Assignments
===========
