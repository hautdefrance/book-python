*********************
About Python Language
*********************


What is Python?
===============

.. figure:: img/python-logo.png
    :scale: 75%
    :align: center

    Python Logo

Python as a Language
--------------------
* Turing complete, general purpose language
* Multi platform
* Dynamic typing with automatic memory allocation and GC
* Code readability and simplicity is important
* White space are important
* Everything is an object, but you can write functional code too

Python as a Community
---------------------
* Standard language in Machine Learning and Data Science
* Very good standard system library
* Huge ecosystem of external open source libraries
* Open Source created by non-profit Python Software Foundation


Which version?
==============
* newest Python 3

What changed in Python 3?
-------------------------
* All strings are Unicode
* Changes in standard library naming
* In Python 3 ``print()`` is a function, not a keyword
* New string formatting

Why not Python 2?
-----------------
* Python 2 is no longer developed
* Python 2.7 is the last in 2.x branch
* There won't be Python 2.8 (`PEP 404 <https://legacy.python.org/dev/peps/pep-0404/>`_)
* End of Life for Python 2.7 is 2020 (`PEP 373 <https://legacy.python.org/dev/peps/pep-0373/>`_)

Status
------

+------------------+--------------+-------------+----------------+----------------+-------------------+
| Branch           | Schedule     | Status      | First release  | End-of-life    | Release manager   |
+==================+==============+=============+================+================+===================+
| 3.8              | :pep:`569`   | features    | *2019-10-20*   | *2024-10*      | Łukasz Langa      |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.7              | :pep:`537`   | bugfix      | 2018-06-27     | *2023-06-27*   | Ned Deily         |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.6              | :pep:`494`   | security    | 2016-12-23     | *2021-12-23*   | Ned Deily         |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.5              | :pep:`478`   | security    | 2015-09-13     | *2020-09-13*   | Larry Hastings    |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.4              | :pep:`429`   | end of life | 2014-03-16     | 2019-03-16     | Larry Hastings    |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.3              | :pep:`398`   | end of life | 2012-09-29     | 2017-09-29     | Georg Brandl      |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.2              | :pep:`392`   | end of life | 2011-02-20     | 2016-02-20     | Georg Brandl      |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.1              | :pep:`375`   | end of life | 2009-06-27     | 2012-04-09     | Benjamin Peterson |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 3.0              | :pep:`361`   | end of life | 2008-12-03     | 2009-01-13     | Barry Warsaw      |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 2.7              | :pep:`373`   | bugfix      | 2010-07-03     | *2020-01-01*   | Benjamin Peterson |
+------------------+--------------+-------------+----------------+----------------+-------------------+
| 2.6              | :pep:`361`   | end of life | 2008-10-01     | 2013-10-29     | Barry Warsaw      |
+------------------+--------------+-------------+----------------+----------------+-------------------+

Scripts
=======

File types and extensions
-------------------------
* Python files use ``.py`` as an extension
* Compiled files are in ``__pycache__`` directory
* Python also uses other extensions:

    .. csv-table:: Python file types and extensions
        :header-rows: 1
        :widths: 15, 85
        :file: data/extensions.csv

Minimal script
--------------
.. code-block:: python

    print('Ehlo World!')

Interpreter declaration
-----------------------
* Declare interpreter for standalone scripts ``#!/usr/bin/env python3``

    .. code-block:: python

        #!/usr/bin/env python3

        print('Ehlo World!')

System environment variable ``PATH``
------------------------------------
* While installing Python, add its executable to one of system ``$PATH`` directories

System environment variable ``PYTHON_PATH``
-------------------------------------------
* Python search for libraries and modules in directories listed in system ``$PYTHON_PATH``
* ``$PYTHON_PATH`` is a base for ``sys.path``


Python Console (REPL)
=====================
* Read–Eval–Print Loop
* Quickly test and evaluate code
* Lines starts with ``>>>``
* Line continuation starts with ``...``
* Result is printed below
* Open REPL with ``python3`` command in terminal

.. code-block:: console

    $ python3

    Python 3.7.0 (default, Aug 22 2018, 15:22:33)
    [Clang 9.1.0 (clang-902.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Ehlo World!')
    Ehlo World!

.. warning:: In documentation and books you may find ``>>>`` and ``...`` at the beginning of code listing lines

    .. code-block:: python

        if True:
            print(True)
        else:
            print(False)


Jupyter
=======
* Open Source web application REPL
* Very popular in Machine Learning and Data Science world
* Create and share documents that contain live code, equations, visualizations and narrative text
* Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, etc
