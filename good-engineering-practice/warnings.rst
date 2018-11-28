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


Example
=======
.. code-block:: python

    import warnings


    def ariane5():
        warnings.warn('ariane5(), is deprecated, please use ariane6() instead', PendingDeprecationWarning)
        print('Launching rocket Ariane 5')

    def ariane6():
        print('Launching rocket Ariane 6')


    ariane5()
    ariane6()

.. code-block:: console

    $ python __notepad__.py

.. code-block:: console

    $ python -W all __notepad__.py
    __notepad__.py:5: PendingDeprecationWarning: ariane5(), is deprecated, please use ariane6() instead


