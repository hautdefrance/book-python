*****
Types
*****


Type inference
==============
* Static Typing (Java, C++, Swift)

    .. code-block:: java

        String name = new String("José Jiménez")

* Dynamic Typing (Python, PHP, Ruby)

    .. code-block:: python

        # Type inference
        name = 'José Jiménez'
        name = str('José Jiménez')


Type Hinting A.K.A. Type Annotation
===================================
* Since Python 3.5
* ``SyntaxError`` in Python before 3.5
* Two names: type hints and type annotations
* Types are not required, and never will be (quote from Guido van Rossum, Python BDFL)
* To check types you have to use IDE or modules like ``mypy`` or ``pyre-check``
* Types are used extensively in system libraries
* More and more books and documentations use types

Basic types
-----------
.. code-block:: python

    name: str = 'Pan Twardowski'
    age: int = 30
    is_adult: bool = True

Collections
-----------
.. code-block:: python

    my_list: list = list()
    my_set: set = set()
    my_tuple: tuple = tuple()
    my_dict: dict = dict()

.. code-block:: python

    my_list: list = []
    my_set: set = set()
    my_tuple: tuple = ()
    my_dict: dict = {}

.. code-block:: python

    from typing import List, Tuple, Dict, Set


    my_list: List[float] = [5.8, 2.7, 5.1, 1.9]
    my_set: Set[int] = {0, 2, 4}
    my_tuple: Tuple[str] = ('setosa', 'virginica', 'versicolor')
    my_dict: Dict[int, str] = {0: 'setosa', 1: 'virginica': 2: versicolor}

Types do not enforce checking
-----------------------------
* This code will run without any problems
* Although ``mypy`` or ``pyre-check`` will throw error

    .. code-block:: python

        name: int = 'Pan Twardowski'
        age: float = 30
        is_adult: int = True


More advanced topics
====================
.. note:: The topic will be continued in chapter: :ref:`Software Engineering Conventions`
