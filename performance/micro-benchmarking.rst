******************
Micro-benchmarking
******************

    We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil" -- Donald Knuth

Setup
=====
.. code-block:: python

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
    ]


Statements
==========
* Jupyter ``%%timeit``

Code 1
------
* 1.53 µs ± 8.41 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

.. code-block:: python

    fieldnames = set()

    for row in DATA:
        fieldnames.update(row.keys())

Code 2
------
* 2.03 µs ± 49.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python

    %%timeit

    fieldnames = set(key for record in DATA for key in record.keys())

Code 2
------
* 431 ns ± 5.93 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

.. code-block:: python

    fieldnames = set()
    fieldnames.add(key
        for record in DATA
           for key in record.keys())

Code 3
------
* 2.11 µs ± 51 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python

    fieldnames = set()
    fieldnames.update(tuple(x.keys()) for x in DATA)

Code 4
------
* 2.43 µs ± 63.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python

    fieldnames = list()

    for row in DATA:
        for key in row.keys():
            fieldnames.append(key)

    set(fieldnames)
