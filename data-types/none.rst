.. _Logical Types:

********
``None``
********


Defining ``None``
=================
* First letter capitalized, other are lower cased
* Empty value (null)
* It is not ``False`` value
* With ``if`` statements behaves like negative values
* Used for unknown (unset) values

.. code-block:: python

    my_var = None


Logic operators
===============
* Do not use ``==`` or ``!=`` to check ``None`` values

.. csv-table:: Logic operators
    :header-rows: 1
    :widths: 15, 25, 60

    "Operand", "Example", "Description"
    "``x is y``", "``x is None``", "``x`` is the same object as ``y``"
    "``x is not y``", "``x is not None``", "``x`` is not the same object as ``y``"


Assignments
===========

To ``bool`` or not to ``bool``
------------------------------
* Filename: ``types_none.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Wprowadzono zmienne:

    .. code-block:: python

        a = False
        b = True
        c = None

        d = 'a'
        e = '.'
        f = '0'
        g = '0.0'
        h = ''
        i = ' '

        j = 0
        k = 0.0
        l = -0
        m = -0.0+0.0j

        n = int('0')
        o = float('-0')

#. Które zmienne mają wartość ``True``, ``None``, ``False``?
#. Czym się różni ``None`` od ``False``?

:The whys and wherefores:
    * Definiowanie zmiennych
    * Konwersja typów
    * Typy logiczne
