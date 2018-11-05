********
Warnings
********


Usage
=====
.. code-block:: python

    import warnings

    warnings.warn('Wersja API jest już nieaktualna', PendingDeprecationWarning)

.. code-block:: python

    import warnings

    def sumuj(a, b):
        warnings.warn('You should english name ``sum()``.', PendingDeprecationWarning)
        return a + b

    def sum(a, b):
        return a + b


    sumuj(1, 2)
    sum(1, 2)

Running
=======
.. code-block:: console

    $ python -W all filename.py
    filename.py:5: PendingDeprecationWarning: You should english name ``sum()``.
      warnings.warn('You should english name ``sum()``.', PendingDeprecationWarning)
