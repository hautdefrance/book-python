***********
Unittesting
***********

.. figure:: img/geek-and-poke-development-driven-tests.jpg
    :align: center
    :scale: 12%

    Development driven tests

- https://martinfowler.com/articles/microservice-testing/#testing-component-out-of-process-diagram
- https://docs.python.org/3/library/unittest.mock.html


Glossary
========
.. glossary::

    Mock
        In object-oriented programming, mock objects are simulated objects that mimic the behavior of real objects in controlled ways. In a unit test, mock objects can simulate the behavior of complex, real objects and are therefore useful when a real object is impractical or impossible to incorporate into a unit test.

    Stub
        A method stub or simply stub in software development is a piece of code used to stand in for some other programming functionality. A stub may simulate the behavior of existing code (such as a procedure on a remote machine) or be a temporary substitute for yet-to-be-developed code. Stubs are therefore most useful in porting, distributed computing as well as general software development and testing.

    Unittest
        In computer programming, unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures, are tested to determine whether they are fit for use.

Using ``unittest``
==================
.. literalinclude:: src/unittest-typing.py
    :language: python
    :caption: Przykład pokrycia klasy za pomocą ``unittest``.

.. literalinclude:: src/unittest-class.py
    :language: python
    :caption: Przykład pokrycia klasy za pomocą ``unittest``

.. literalinclude:: src/unittest-temperature.py
    :language: python
    :caption: Przykład pokrycia klasy za pomocą ``unittest``

:Usage:
    .. code-block:: console

        $ python -m unittest FILE.py


Assignments
===========

Dragon
------
#. Napisz testy jednostkowe dla Smoka z OOP
