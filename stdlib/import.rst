**********
``import``
**********


Using
=====
``import ...``


Importing
=========
* Imports module:

    .. code-block:: python

        import module

* From module imports function:

    .. code-block:: python

        from module import function
        from module.submodule import function

* Aliases

    .. code-block:: python

        import module as alias
        from module import function as alias

* Relative imports:

    .. code-block:: python

        from . import module
        from .. import module

    .. code-block:: python

        from .module import function
        from ..module import function

Example
-------
.. code-block:: python

    import sys

    sys.path
    sys.path.append
    sys.path.insert(0, '/path/to/directory')

.. code-block:: text

    game
        __init__.py
        config.py
        api.py
        dragon
            __init__.py
            wawelski.py
            red.py
            black.py
            white.py

.. code-block:: python

    from game.config import RESOLUTION_MAX_X

.. code-block:: python

    from game.dragon import red
    from game.dragon import white


    my_dragon1 = red.RedDragon()
    my_dragon2 = white.WhiteDragon()

.. code-block:: python

    from game.dragon import *

    my_dragon1 = red.RedDragon()
    my_dragon2 = white.WhiteDragon()

.. code-block:: python

    from game.dragon.red import RedDragon
    from game.dragon.white import WhiteDragon

    my_dragon1 = RedDragon()
    my_dragon2 = WhiteDragon()

.. code-block:: python

    from game.dragon.red import RedDragon as Smok

    wawelski = Smok()
