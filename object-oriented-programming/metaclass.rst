.. _Metaclass:

*********
Metaclass
*********

    “Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don’t (the people who actually need them know with certainty that they need them, and don’t need an explanation about why).” -- Tim Peters

.. code-block:: python

    >>> for t in int, float, dict, list, tuple:
    ...     print(type(t))
    ...
    <class 'type'>
    <class 'type'>
    <class 'type'>
    <class 'type'>
    <class 'type'>

.. code-block:: python

    >>> type(type)
    <class 'type'>

.. figure:: img/metaclass-class-chain.png
    :scale: 75%
    :align: center

A metaclass is the class of a class. Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass.

.. figure:: img/metaclass-instances.png
    :scale: 75%
    :align: center

    A metaclass is the class of a class. Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves. A class is an instance of a metaclass.

A metaclass is most commonly used as a class-factory. Like you create an instance of the class by calling the class, Python creates a new class (when it executes the 'class' statement) by calling the metaclass. Combined with the normal ``__init__`` and ``__new__`` methods, metaclasses therefore allow you to do 'extra things' when creating a class, like registering the new class with some registry, or even replace the class with something else entirely.

When the ``class`` statement is executed, Python first executes the body of the ``class`` statement as a normal block of code. The resulting namespace (a dict) holds the attributes of the class-to-be. The metaclass is determined by looking at the baseclasses of the class-to-be (metaclasses are inherited), at the ``__metaclass__`` attribute of the class-to-be (if any) or the ``__metaclass__`` global variable. The metaclass is then called with the name, bases and attributes of the class to instantiate it.

However, metaclasses actually define the *type* of a class, not just a factory for it, so you can do much more with them. You can, for instance, define normal methods on the metaclass. These metaclass-methods are like classmethods, in that they can be called on the class without an instance, but they are also not like classmethods in that they cannot be called on an instance of the class. ``type.__subclasses__()`` is an example of a method on the ``type`` metaclass. You can also define the normal 'magic' methods, like ``__add__``, ``__iter__`` and ``__getattr__``, to implement or change how the class behaves.

.. code-block:: python

    >>> class Foo:
    ...     pass
    ...
    >>> f = Foo()

The ``__call__()`` method of Foo’s parent class is called. Since Foo is a standard new-style class, its parent class is the type metaclass, so type’s ``__call__()`` method is invoked.

That ``__call__()`` method in turn invokes the following:

    - ``__new__()``
    - ``__init__()``

If Foo does not define ``__new__()`` and ``__init__()``, default methods are inherited from Foo’s ancestry. But if Foo does define these methods, they override those from the ancestry, which allows for customized behavior when instantiating Foo.

.. code-block:: python

    >>> def new(cls):
    ...     x = object.__new__(cls)
    ...     x.attr = 100
    ...     return x
    ...
    >>> Foo.__new__ = new

    >>> f = Foo()
    >>> f.attr
    100

    >>> g = Foo()
    >>> g.attr
    100

.. code-block:: python

    # Spoiler alert:  This doesn't work!
    >>> def new(cls):
    ...     x = type.__new__(cls)
    ...     x.attr = 100
    ...     return x
    ...
    >>> type.__new__ = new
    Traceback (most recent call last):
      File "<pyshell#77>", line 1, in <module>
        type.__new__ = new
    TypeError: can't set attributes of built-in/extension type 'type'

.. code-block:: python

    >>> class Meta(type):
    ...     def __new__(cls, name, bases, dct):
    ...         x = super().__new__(cls, name, bases, dct)
    ...         x.attr = 100
    ...         return x
    ...

.. code-block:: python

    >>> class Foo(metaclass=Meta):
    ...     pass
    ...
    >>> Foo.attr
    100

.. code-block:: python

    >>> class Bar(metaclass=Meta):
    ...     pass
    ...
    >>> class Qux(metaclass=Meta):
    ...     pass
    ...
    >>> Bar.attr, Qux.attr
    (100, 100)

As simple as the above class factory example is, it is the essence of how metaclasses work. They allow customization of class instantiation.

In Python, there are at least a couple other ways in which effectively the same thing can be accomplished:

    - Simple Inheritance
    - Class Decorator

.. code-block:: python

    >>> class Base:
    ...     attr = 100
    ...
    ...
    >>> class X(Base):
    ...     pass
    ...
    ...
    >>> X.attr
    100

.. code-block:: python

    >>> def decorator(cls):
    ...     class NewClass(cls):
    ...         attr = 100
    ...     return NewClass
    ...
    >>> @decorator
    ... class X:
    ...     pass
    ...
    >>> X.attr
    100
