.. _Introspection:

************
Introspekcja
************


``eval``
========
.. code-block:: python

    x = 1
    eval('x+1')  # 2



Pola obiektu
============
* ``__dict__``

.. code-block:: python

    from pprint import pprint

    class Server:
        _connection = None

        def __init__(self, host, port):
            self.host = host
            self.port = port

    localhost = Server(host='127.0.0.1', port=1337)
    output = localhost.__dict__
    print(f'Listowanie pól za pomocą dict: {output}')


    pola = [x for x in dir(Server) if not x.startswith('__')]
    print(f'Listowanie pól klasy: {pola}')

    zmienne = vars(Server)
    print(f'Listowanie za pomoca vars(): {zmienne}')

Metody obiektu
==============
* ``dir()``

.. code-block:: python

    class Server:
        _connection = None

        def __init__(self, host, port):
            self.host = host
            self.port = port

    localhost = Server(host='127.0.0.1', port=1337)
    output = dir(localhost)
    print(output)


``help()``
----------
* ``help()``

.. code-block:: python

    class Server:
        _connection = None

        def __init__(self, host, port):
            self.host = host
            self.port = port

    localhost = Server(host='127.0.0.1', port=1337)
    output = help(localhost)
    print(output)

Introspekcja obiektów
=====================
In computer programming, introspection is the ability to determine the
type of an object at runtime. It is one of Python's strengths.
Everything in Python is an object and we can examine those objects.
Python ships with a few built-in functions and modules to help us.

``dir``
-------
Returns a list of attributes and methods belonging to an object.

.. code-block:: python

    my_list = [1, 2, 3]
    dir(my_list)
    # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
    # '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    # '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
    # '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
    # '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
    # '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
    # '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
    # 'remove', 'reverse', 'sort']

Our introspection gave us the names of all the methods of a list. This
can be handy when you are not able to recall a method name. If we run
``dir()`` without any argument then it returns all names in the current
scope.

``type`` and ``id``
-------------------
The ``type`` function returns the type of an object. For example:

.. code-block:: python

    print(type(''))
    # Output: <type 'str'>

    print(type([]))
    # Output: <type 'list'>

    print(type({}))
    # Output: <type 'dict'>

    print(type(dict))
    # Output: <type 'type'>

    print(type(3))
    # Output: <type 'int'>

``id`` returns the unique ids of various objects. For instance:

.. code-block:: python

    name = "Yasoob"
    print(id(name))
    # Output: 139972439030304

``isinstance()``
----------------

``inspect`` module
------------------

The inspect module also provides several useful functions to get
information about live objects. For example you can check the members of
an object by running:

.. code-block:: python

    import inspect
    print(inspect.getmembers(str))
    # Output: [('__add__', <slot wrapper '__add__' of ... ...

There are a couple of other methods as well which help in introspection.
You can explore them if you wish.

``vars()``
----------


Other
=====

.. code-block:: python

    import settings
    from django.db import models

    for app in settings.INSTALLED_APPS:
        models_name = app + ".models"

        try:
            models_module = __import__(models_name, fromlist=["models"])
            attributes = dir(models_module)

            for attr in attributes:
                try:
                    attrib = models_module.__getattribute__(attr)
                    if issubclass(attrib, models.Model) and attrib.__module__== models_name:
                    print "%s.%s" % (models_name, attr)
                except TypeError, e:
                    pass
        except ImportError, e:
            pass

.. code-block:: python

    from django.contrib import admin
    from . import models
    import inspect

    for name, obj in inspect.getmembers(models):
        if inspect.isclass(obj):
            admin.site.register(getattr(models, name))

