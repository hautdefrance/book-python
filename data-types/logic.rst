.. _Logical Types:

*************
Logical Types
*************


``bool``
========
* ``True`` - Positive value
* ``False`` - Negative value
* First letter capitalized, other are lower cased

Defining ``bool``
-----------------
.. code-block:: python

    my_var = True
    my_var = False

    my_var: bool = True
    my_var: bool = False

Converting to ``bool``
----------------------
* Also known as "type casting"
* ``float()`` converts argument to ``float``

.. code-block:: python

    bool(1)               # True
    bool(0)               # False

.. code-block:: python

    bool(1.0)             # True
    bool(0.0)             # False

.. code-block:: python

    bool('José')          # True
    bool('')              # False

Negative values
---------------
* ``False``
* ``0``
* ``0.0``
* ``()`` - empty ``tuple``
* ``{}`` - empty ``dict``
* ``[]`` - empty ``list``
* ``''`` - empty ``str``
* ``set()`` - empty ``set``
* ``None``

Using ``and``
-------------
.. code-block:: python

    1 and 1               # True
    1 and 0               # False
    0 and 0               # False

.. code-block:: python

    'José' and 'Иван'     # True
    'José' and ''         # False
    '' and ''             # False

Using ``or``
------------
.. code-block:: python

    1 or 1                # True
    1 or 0                # True
    0 or 0                # False

.. code-block:: python

    'José' or 'Иван'      # True
    'José' or ''          # True
    '' or ''              # False


``None``
========
* First letter capitalized, other are lower cased
* Empty value (null)
* It is not ``False`` value
* With ``if`` statements behaves like negative values
* Used for unknown (unset) values

Defining ``None``
-----------------
.. code-block:: python

    my_var = None


Assignments
===========

Bool
----
#. Wprowadzono zmienne:

    .. code-block:: python

        a = False
        b = True
        c = None
        d = ''
        e = ' '
        f = 'a'
        g = '.'
        h = 0
        i = 0.0
        j = '0'
        k = '0.0'
        l = -0
        m = -0.0+0.0j
        n = int('0')
        o = float('0')

#. Które zmienne mają wartość ``True``, ``None``, ``False``?
#. Czym się różni ``None`` od ``False``?

:About:
    * Filename: ``types_bool.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Konwersja typów
    * Typy logiczne
