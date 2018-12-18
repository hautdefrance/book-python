************
C Extensions
************

* biblioteka ``ctypes``
* C Modules

C Types
=======

Kompilacja
----------
.. code-block:: console

    $ include_dir='-I/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/include/python3.6m/'
    $ gcc -fPIC -c -o mylib-ctypes.o mylib-ctypes.c ${include_dir}
    $ gcc -shared mylib-ctypes.o -o mylib-ctypes.so

Przykład - Rekurencja
---------------------
.. code-block:: C

    long factorial(long n) {
        if (n == 0)
            return 1;

        return (n * factorial(n - 1));
    }

.. code-block:: python

    import ctypes

    lib = ctypes.CDLL('mylib-ctypes.so')

    lib.factorial(16)  # 2004189184
    lib.factorial(17)  # -288522240

Argumenty
---------
* ``ctypes.c_double``
* ``ctypes.c_int``
* ``ctypes.c_char``
* ``ctypes.c_char_p``
* ``ctypes.POINTER(ctypes.c_double)``

.. code-block:: python

    lib.my_function.argtypes = [
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_double),
    ]

    lib.my_function.restype = ctypes.c_char_p

Przykład - typy proste
----------------------

.. code-block:: C

    #include <stdio.h>

    void ehlo() {
        printf("Ehlo World");
    }

    void greeting(char *name) {
        printf("Ehlo %s!\n", name);
    }

    void number(int num) {
        printf("My number %d\n", num);
    }

    int return_int(int num) {
        return num;
    }

.. code-block:: python

    import ctypes
    lib = ctypes.CDLL('mylib-ctypes.so')

    lib.ehlo()

    lib.greeting.argtypes = [ctypes.c_char_p]
    name = ctypes.create_string_buffer('Twardowski'.encode('ASCII'))
    lib.greeting(name)

    lib.number(10)

    print(dir(lib))

    i = lib.return_int(15)
    print(i)

Wywołania funkcji
-----------------

.. code-block:: python

    import sys
    import ctypes


    if sys.platform == 'darwin':
       lib = ctypes.CDLL('/usr/lib/libc.dylib')
    elif sys.platform == 'win32':
        lib = ctypes.CDLL('/usr/lib/libc.dll')
    else:
        lib = ctypes.CDLL('/usr/lib/libc.so')


    lib.printf("I'm C printf() function called from Python")

Overflow
--------

.. code-block:: C

    #include <stdio.h>

    void wypisz_liczbe(int liczba) {
        printf("Liczba to: %d", liczba);
    }

.. code-block:: python

    import ctypes

    lib = ctypes.CDLL('biblioteka.so')

    lib.wypisz_liczbe(10 ** 10)  # Liczba to: 1410065408

    lib.wypisz_liczbe(10 ** 30)
    # Traceback (most recent call last):
    #   ...
    # ctypes.ArgumentError: argument 1: <class 'OverflowError'>: int too long to convert


C Modules
=========

Python 3
--------
.. literalinclude:: src/c-modules.c
    :name: listing-c-modules
    :language: C
    :caption: Przykład kodu w C wykorzystującego *C modules*

``setup.py``
------------

.. code-block:: python

    import sys
    from distutils.core import setup, Extension

    if sys.version_info >= (3,):
        print('Building for Python 3')
        module = Extension('hello', sources = ['hello-py3.c'])

    elif sys.version_info >= (2,):
        print('Building for Python 2')
        module = Extension('hello', sources=['hello-py2.c'])

    else:
        print('Unsupported Python version')
        sys.exit(1)

    setup(
        name = 'hello',
        version='1.0',
        description = 'Ehlo World!',
        ext_modules = [module])

.. code-block:: console

    $ python setup.py build

    $ cd build/lib*

    $ python

.. code-block:: python

    import hello
    hello.say_hello('José Jiménez')


Assignments
===========

C Types
-------
* Filename: ``cext_types.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

Wykorzystując C Types wyświetl na ekranie datę i czas, za pomocą funkcji zdefiniowanej w C ``<time.h>``

C Modules
---------
* Filename: ``cext_modules.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

Wykorzystując C Modules wyświetl na ekranie datę i czas, za pomocą funkcji zdefiniowanej w C ``<time.h>``
