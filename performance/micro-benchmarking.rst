******************
Micro-benchmarking
******************

    We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil" -- Donald Knuth


Evaluation
==========
* Fresh start of Python process
* Clean memory before start
* Same data
* Same start conditions, CPU load, RAM usage, ``iostat``
* Do not measure how long Python wakes up
* Check what you measure

.. _timeit:

``timeit``
==========

Programmatic use
----------------
.. literalinclude:: src/utils-timeit-simple.py
    :language: python
    :caption: Timeit simple statement

.. literalinclude:: src/utils-timeit-multiple.py
    :language: python
    :caption: Timeit multiple statements with setup code

.. literalinclude:: src/utils-timeit-globals.py
    :language: python
    :caption: Timeit with ``globals()``

Console use
-----------
.. literalinclude:: src/utils-timeit.sh
    :language: console
    :caption: Timeit

.. code-block:: text

    -n N, --number=N
    how many times to execute ‘statement’

    -r N, --repeat=N
    how many times to repeat the timer (default 5)

    -s S, --setup=S
    statement to be executed once initially (default pass)

    -p, --process
    measure process time, not wallclock time, using time.process_time() instead of time.perf_counter(), which is the default

    -u, --unit=U
    specify a time unit for timer output; can select nsec, usec, msec, or sec

    -v, --verbose
    print raw timing results; repeat for more digits precision

    -h, --help
    print a short usage message and exit


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

    fieldnames = set(key for record in DATA for key in record.keys())

Code 3
------
* 431 ns ± 5.93 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

.. code-block:: python

    fieldnames = set()
    fieldnames.add(key
        for record in DATA
           for key in record.keys())

.. warning:: Is it correct?

Code 4
------
* 2.11 µs ± 51 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python

    fieldnames = set()
    fieldnames.update(tuple(x.keys()) for x in DATA)

Code 5
------
* 2.43 µs ± 63.9 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python

    fieldnames = list()

    for row in DATA:
        for key in row.keys():
            fieldnames.append(key)

    set(fieldnames)


Summary
=======
* Code 3 appends generator object not values, this is why it is so fast!


References
==========
* https://www.youtube.com/watch?v=RT88FrHttRI
