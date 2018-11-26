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
