.. _Advanced Functions:

******************
Advanced Functions
******************


Type annotations
================
* Od Python 3.5
* Kod w języku python wykona się nawet jeśli typ nie zgadza się z adnotacją!
* Twoje IDE porówna typy oraz poinformuje cię jeżeli wykryje niezgodność
* Użyj ``mypy`` lub ``pyre-check`` do sprawdzania typów

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add(1, 2.5)
    # 3.5

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add('José', 'Jiménez')
    # 'JoséJiménez'

.. note:: więcej na ten temat w rozdziale dotyczącym :ref:`Type Annotation`


Callable
========
.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    hello                 # <function hello at 0x0C55D420>
    type(hello)           # <class 'function'>
    hello()               # My name... José Jiménez

.. code-block:: python

    'hello'               # 'hello'
    type('hello')         # <class 'str'>
    'hello'()             # TypeError: 'str' object is not callable

Returning function (callable)
-----------------------------
.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    def function():
        return hello

    my_name = function()  # <function __main__.hello()>
    my_name()             # My name... José Jiménez

.. code-block:: python

    import datetime
    import time

    now = datetime.datetime.now()

    print(now)            # 1969-07-21 14:56:15
    time.sleep(10)
    print(now)            # 1969-07-21 14:56:15

.. code-block:: python

    import datetime
    import time

    now = datetime.datetime.now

    print(now())          # 1969-07-21 14:56:15
    time.sleep(10)
    print(now())          # 1969-07-21 14:56:25


Assignments
===========
