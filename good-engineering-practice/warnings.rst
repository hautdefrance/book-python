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

Example 2
---------
.. code-block:: python

    import warnings
    import functools


    def deprecated(func):
        """
        This is a decorator which can be used to mark functions
        as deprecated. It will result in a warning being emitted
        when the function is used.
        """

        @functools.wraps(func)
        def new_func(*args, **kwargs):
            warnings.warn_explicit(
                f"Call to deprecated function {func.__name__}.",
                category=DeprecationWarning,
                filename=func.func_code.co_filename,
                lineno=func.func_code.co_firstlineno + 1)
            return func(*args, **kwargs)
        return new_func


    ## Usage examples ##
    @deprecated
    def my_func():
        pass

    @other_decorators_must_be_upper
    @deprecated
    def my_func():
        pass

Example 3
---------
.. code-block:: python

    import warnings


    class RemovedInVersion20(DeprecationWarning):
        pass


    def sumuj(a, b):
        warnings.warn('Use ``sum`` function', RemovedInVersion20)
        return a + b

    def sum(a, b):
        return a + b


    sumuj(1, 2)
    sum(1, 2)
