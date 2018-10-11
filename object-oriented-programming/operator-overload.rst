*****************
Operator Overload
*****************


Why to use operator overload?
=============================
* Readable syntax
* Simpler operations

Example usage of operator Overload
----------------------------------
.. code-block:: python

    class Vector:
        def __init__(self, x=0.0, y=0.0):
            self.x = x
            self.y = y

        def __str__(self):
            return f'Vector(x={self.x}, y={self.y})'

        def __add__(self, other):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    vector1 = Vector(x=1, y=2)
    vector2 = Vector(x=3, y=4)
    suma = vector1 + vector2

    print(suma)
    # Vector(x=4, y=6)

.. code-block:: python

    import math

    class Vector:
        def __init__(self, x=0.0, y=0.0):
            self.x = x
            self.y = y

        def __abs__(self):
            return math.sqrt(self.x**2 + self.y**2)


Numerical Operator Overload
===========================
.. csv-table:: Operator Overload
    :header-rows: 1

    "Operator", "Description"
    "``__add__()``", "``a + b``"
    "``__iadd__()``", "``a += b``"
    "``__sub__()``", "``a - b``"
    "``__isub__()``", "``a -= b``"
    "``__mul__()``", "``a * b``"
    "``__imul__()``", "``a *= b``"
    "``__div__()``", "``a / b``"
    "``__idiv__()``", "``a /= b``"
    "``__mod__()``", "``a % b``"
    "``__divmod__()``", "``divmod(a, b)``"
    "``__abs__()``", "``abs(a)``"
    "``__pow__()``", "``pow(a)``"
    "``__round__()``", "``round(a)``, or ``round(a, x)``, where ``x`` is ndigits presision"


Logical Operator Overload
=========================
.. csv-table:: Operator Overload
    :header-rows: 1

    "Operator", "Description"
    "``__eq__()``", "``a == b``"
    "``__ne__()``", "``a != b``"
    "``__lt__()``", "``a < b``"
    "``__le__()``", "``a <= b``"
    "``__gt__()``", "``a > b``"
    "``__ge__()``", "``a >= b``"
    "``__bool__()``", "``bool(a)``"
    "``__neg__()``", "``-a``"
    "``__pos__``", "``+a``"


Boolean Operator Overload
=========================
.. csv-table:: Operator Overload
    :header-rows: 1

    "Operator", "Description"
    "``__and__()``", "``a & b``"
    "``__or__()``", "``a | b``"
    "``__xor__()``", "``a ^ b``"
    "``__lshift__()``", "``a << b``"
    "``__rshift__()``", "``a >> b``"


Builtins Function Overload
==========================
.. csv-table:: Operator Overload
    :header-rows: 1

    "Operator", "Description"
    "``__dir__()``", "``dir(a)``"
    "``__len__()``", "``len(a)``"
    "``__delattr__()``", "``delattr(cls, 'a')`` or ``del a``"
    "``__complex__()``", "``complex(a)``"
    "``__int__()``", "``int(a)``"
    "``__float__()``", "``float(a)``"
    "``__oct__()``", "``oct(a)``"
    "``__hex__()``", "``hex(a)``"
    "``__reversed__()``", "``reversed()``"


Accessors Overload
==================
.. csv-table:: Operator Overload
    :header-rows: 1

    "Operator", "Description"
    "``__getitem__()``", "``a[b]``"
    "``__setitem__()``", "``a[b] = 10``"
    "``__contains__()``", "``a in b``"
    "``__missing__()``", "``a[b]`` when ``b`` is not in ``a``"


Assignment
==========

Address Book
------------
#. Dopisz odpowiednie metody do ``Contact`` i ``Address`` aby poniższy kod zadziałał poprawnie

:About:
    * Filename: ``oop_addressbook_operators.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 15 min

.. code-block:: python

    class Contact:
        def __str__(self):
            return f'{self.__dict__}'


    class Address:
        def __repr__(self):
            return f'{self.__dict__}'


    contact = Contact(name='José Jiménez', addresses=[Address(location='JPL')])
    contact += Address(location='Houston')
    contact += Address(location='KSC')

    print(contact)
    # {'name': 'José Jiménez', 'addresses': [
    #       {'location': 'JPL'},
    #       {'location': 'Houston'},
    #       {'location': 'KSC'}
    # ]}

    if Address(location='Bajkonur') in contact:
        print(True)
    else:
        print(False)
    # False
