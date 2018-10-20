.. _Syntax:

******
Syntax
******


Indentation instead of braces
=============================
* Python uses indentation instead of braces
* `4 spaces indentation, no tabs <https://youtu.be/SsoOG6ZeyUI>`_
* Python throws ``IndentationError`` exception on problem
* Code indented on the same level belongs to block:

    .. code-block:: python

        if True:
            print('First line of the true statement')
            print('Second line of the true statement')
            print('Third line of the true statement')
        else:
            print('This is false')


End of lines
============
* No semicolon (``;``) at the end of lines
* ``\r\n`` and ``\n`` are good:

    .. code-block:: python

        print('Hello!\nHow are you?')
        print('Hello!\r\nHow are you?')

Comments
========

Line comments
---------------
* Indent must be on the same level as block indent
* Hash (``#``), space and then comment:

    .. code-block:: python

        # José Jiménez says hello
        print('My name... José Jiménez')

Inline comments
---------------
* Source code, two spaces, hash (``#``), space and then comment:

    .. code-block:: python

        print('My name... José Jiménez')  # José Jiménez says hello

Multiline comments
------------------
* Both single and double are good
* Triple single quotes ``'''``
* Triple double quotes ``"""``
* Triple double quotes are more common:

    .. code-block:: python

        """
        We choose to go to the Moon!
        We choose to go to the Moon in this decade and do the other things,
        not because they are easy, but because they are hard;
        because that goal will serve to organize and measure the best of our energies and skills,
        because that challenge is one that we are willing to accept, one we are unwilling to postpone,
        and one we intend to win, and the others, too.
        """

Docstring
---------
* Docstring is a first multiline comment in:

    * File / Module
    * Class
    * Method / Function

* It is accessible in ``__doc__`` property of an object
* Used for generating ``help()`` documentation

    .. code-block:: python

        def apollo_dsky(noun, verb):
            """
            This is the Apollo Display Keyboard
            It takes noun and verb
            """
            print(f'Program selected. Noun: {noun}, verb: {verb}')

* Used for ``doctest``

    .. code-block:: python

        def add(a, b):
            """
            Sums two numbers.

            >>> add(1, 2)
            3
            """
            return a + b

Commented out code
------------------
* Never!
* Use Version Control System instead - e.g.: ``git blame``
* IDE has Local history (modifications) and you can compare file


Variables and constants
=======================
* ``NameError`` when using not declared variable
* ``AttributeError`` when cannot assign to variables

Variable declaration
--------------------
* Lowercase letters for variable names

    .. code-block:: python

        name = 'José Jiménez'

* Underscore ``_`` is used for multi-word names

    .. code-block:: python

        first_name = 'José'
        last_name = 'Jiménez'

Constant declaration
--------------------
* Uppercase letters for constants names

    .. code-block:: python

        PATH = '/etc/passwd'

* Underscore ``_`` is used for multi-word names

    .. code-block:: python

        FILE_NAME = '/etc/shadow'

Variables vs. constants
-----------------------
* Python do not distinguish between variables and constants
* Python allows you to change "constants" but it's a bad practice

Type inference
--------------
* Static Typing (Java, C++, Swift)

    .. code-block:: java

        String name = new String("José Jiménez")

* Dynamic Typing (Python, PHP, Ruby)

    .. code-block:: python

        # Type inference
        name = 'José Jiménez'
        name = str('José Jiménez')

Types
-----
* Since Python 3.5
* ``SyntaxError`` in Python before 3.5
* Two names: type hints and type annotations
* Types are not required, and never will be (quote from Guido van Rossum, Python BDFL)
* To check types you have to use IDE or modules like ``mypy`` or ``pyre-check``
* Types are used extensively in system libraries
* More and more books and documentations use types
* Declaring objects with types:

    .. code-block:: python

        name: str = 'José Jiménez'
        age: int = 30

* Types do not enforce checking:

    .. code-block:: python

        # This code will run without any problems
        # Although ``mypy`` or ``pyre-check`` will throw error
        name: int = 'José Jiménez'
        age: float = 30


More advanced topics
====================
.. note:: The topic will be continued in chapter: :ref:`Software Engineering Conventions`


Assignments
===========

Meet Python
-----------
#. Create Python script
#. Add interpreter declaration
#. Under interpreter declaration add multiline comment with program description (copy-paste from book)
#. Declare variable ``name`` and set its value to your name
#. Add inline comment to variable declaration with text: "This is my name"
#. Print variable
#. Next line under ``print`` statement add line comment, with expected output
#. Run script

:About:
    * Filename: ``syntax_python.py``
    * Lines of code to write: 2 lines + 2 lines of comment
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * Tworzenie skryptów Python
    * Deklaracja zmiennych
    * Komentowanie kodu
    * Wyświetlanie wartości zmiennych

:Hint:
    * ``print()``
