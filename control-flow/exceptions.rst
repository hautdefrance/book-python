.. _Exceptions:

**********
Exceptions
**********


What are and why to use exceptions?
===================================
* Used when error occurs
* You can catch exception and handles erroneous situation
* Exception example situations:

    * File does not exists
    * Function argument is invalid
    * Network or database connection could not be established


Most common exceptions
======================
.. csv-table:: Most common exceptions
    :header-rows: 1
    :widths: 25, 75
    :file: data/exception-most-common.csv

AttributeError
--------------
.. code-block:: python

    name = 'Jose'

    name.append('Jimenez')
    # AttributeError: 'str' object has no attribute 'append'

ImportError, ModuleNotFoundError
--------------------------------
.. code-block:: python

    import math

.. code-block:: python

    import match
    # ModuleNotFoundError

IndexError
----------
.. code-block:: python

    DATA = ['a', 'b', 'c']

    DATA[100]
    # IndexError: list index out of range

KeyError
--------
.. code-block:: python

    DATA = {'a': 1, 'b': 2}

    DATA['x']
    # KeyError: 'x'

NameError
---------
.. code-block:: python

    print(first_name)
    # NameError: name 'first_name' is not defined

SyntaxError
-----------
.. code-block:: python

    if True
        print('Yes')

    # SyntaxError: invalid syntax

IndentationError
----------------
.. code-block:: python

    if True:
       print('Hello!')
        print('My name...')
       print('Jose Jimenez')

    # IndentationError: unexpected indent

TypeError
---------
.. code-block:: python

    42 + 'Jose'
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

ValueError
----------
.. code-block:: python

    float('hello')
    # ValueError: could not convert string to float: 'hello'


Raising exceptions
==================

Simple Exception
----------------
.. code-block:: python

    raise RuntimeError

Exception with additional message
---------------------------------

.. code-block:: python

    raise RuntimeError('Some message')

Use case
--------
.. code-block:: python

    def apollo18():
        raise NotImplementedError('Mission dropped due to budget cuts')

    def apollo13():
        raise RuntimeError('Mid-flight Oxygen tank explosion')


    apollo18()
    apollo13()


Traceback analysis
==================
.. code-block:: python

    def apollo13():
        raise RuntimeError('Mid-flight Oxygen tank explosion')

    apollo13()

* Stacktraces are 8 levels deep, it's not Java's 200 ;)

    .. code-block:: text

          File "/Users/matt/.virtualenvs/book-python/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 2961, in run_code
            exec(code_obj, self.user_global_ns, self.user_ns)
          File "<ipython-input-2-badb71482ca2>", line 1, in <module>
            runfile('/Users/matt/Developer/book-python/__notepad__.py', wdir='/Users/matt/Developer/book-python')
          File "/Applications/PyCharm 2018.3 EAP.app/Contents/helpers/pydev/_pydev_bundle/pydev_umd.py", line 198, in runfile
            pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
          File "/Applications/PyCharm 2018.3 EAP.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
            exec(compile(contents+"\n", file, 'exec'), glob, loc)
          File "/Users/matt/Developer/book-python/__notepad__.py", line 13, in <module>
            apollo13()
          File "/Users/matt/Developer/book-python/__notepad__.py", line 5, in apollo13
            raise RuntimeError('Mid-flight Oxygen tank explosion')
        RuntimeError: Mid-flight Oxygen tank explosion

* Change level with ``sys.tracebacklimit``:

    .. code-block:: python

        import sys
        sys.tracebacklimit = 1

* From time to time you can have problems somewhere in the middle, but it's rare
* Last lines are the most important, in most cases error is there

    .. code-block:: text

          File "/Users/matt/Developer/book-python/__notepad__.py", line 5, in apollo13
            raise RuntimeError('Mid-flight Oxygen tank explosion')
        RuntimeError: Mid-flight Oxygen tank explosion


Catching exceptions
===================
* ``try``
* ``except``
* ``else``
* ``finally``

Catch single exception
----------------------
.. code-block:: python

    def apollo13():
        raise RuntimeError('Mid-flight Oxygen tank explosion')


    try:
        apollo13()
    except RuntimeError:
        print('Houston we have a problem!')

Catch many exceptions with the same handling
--------------------------------------------
.. code-block:: python

    def apollo13():
        raise RuntimeError('Mid-flight Oxygen tank explosion')


    try:
        apollo13()
    except (RuntimeError, TypeError, NameError):
        print('Houston we have a problem!')

Catch many exceptions with different handling
---------------------------------------------
.. code-block:: python

    def open_file(path):
        if path.startswith('/tmp/'):
            print('Will make file')
        elif path.startswith('/etc/'):
            raise PermissionError('Permission Denied')
        else:
            raise FileNotFoundError('File not found')


    try:
        open_file('/etc/my-file.txt')
    except FileNotFoundError:
        print('Permission Denied')
    except PermissionError:
        print('File not found')

Exceptions logging
------------------
.. code-block:: python

    import logging

    def open_file(filename):
        raise PermissionError('Permission Denied')


    try:
        open_file('/tmp/my-file.txt')
    except PermissionError as err:
        logging.error(err)

.. code-block:: python

    def apollo11():
        print('Program P63 - Landing Maneuvre Approach Phase')
        raise RuntimeError('1201 Alarm')
        raise RuntimeError('1202 Alarm')
        print('Contact lights')
        print('The Eagle has landed!')
        print("That's one small step for [a] man, one giant leap for mankind.")


    try:
        apollo11()

    except RuntimeError:
        print("Yo're GO for landing")

    except Exception:
        print('Abort')

    else:
        print('Landing a man on the Moon')

    finally:
        print('Returning safely to the Earth')

.. warning:: Always catch exception!

    .. code-block:: python

        # Problematic code which catches 'Ctrl-C'
        # User cannot simply kill program
        while True:
            try:
                number = float(input('Type number: '))
            except:
                continue

    .. code-block:: python

        # User can kill program with 'Ctrl-C'
        while True:
            try:
                number = float(input('Type number: '))
            except Exception:
                continue


Exception hierarchy
===================
.. code-block:: text

    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning


Defining own exceptions
=======================
.. code-block:: python

    import math


    class CotangentDoesNotExistsError(ArithmeticError):
        pass


    def cotangent(degrees):
        if degrees == 180:
            raise CotangentDoesNotExistsError('Cotangent for 180 degrees is infinite')

        radians = math.radians(degrees)
        return 1 / math.tan(radians)


    cotangent(180)
    # CotangentDoesNotExistsError: Cotangent for 180 degrees is infinite


Real life use-case
==================
.. code-block:: python

    from django.contrib.auth.models import User

    try:
        User.objects.get(username='jose-jimenez')
    except User.DoesNotExists:
        print('No such user')
