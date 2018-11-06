****************************
Commandline argument parsing
****************************


``argparse``
============
* https://docs.python.org/3/library/argparse.html#the-add-argument-method
* Define how a single command-line argument should be parsed.

Parser parameters
-----------------
.. csv-table::
    :header-rows: 1

    "prog", "The name of the program (default: ``sys.argv[0]``)"
    "usage", "A usage message (default: auto-generated from arguments)"
    "description", "A description of what the program does"
    "epilog", "Text following the argument descriptions"
    "parents", "Parsers whose arguments should be copied into this one"
    "formatter_class", "HelpFormatter class for printing help messages"
    "prefix_chars", "Characters that prefix optional arguments"
    "fromfile_prefix_chars", "Characters that prefix files containing additional arguments"
    "argument_default", "The default value for all arguments"
    "conflict_handler", "String indicating how to handle conflicts"
    "add_help", "Add a -h/-help option"
    "allow_abbrev", "Allow long options to be abbreviated unambiguously"

Argument parameters
-------------------
.. csv-table::
    :header-rows: 1

    "parameter", "description"
    "name or flags", "Either a name or a list of option strings, e.g. foo or ``-f``, ``--foo``"
    "action", "The basic type of action to be taken when this argument is encountered at the command line"
    "nargs", "The number of command-line arguments that should be consumed"
    "const", "A constant value required by some action and nargs selections"
    "default", "The value produced if the argument is absent from the command line"
    "type", "The type to which the command-line argument should be converted"
    "choices", "A container of the allowable values for the argument"
    "required", "Whether or not the command-line option may be omitted (optionals only)"
    "help", "A brief description of what the argument does"
    "metavar", "A name for the argument in usage messages"
    "dest", "The name of the attribute to be added to the object returned by ``parse_args()``"

Simple parsing
--------------
.. code-block:: python

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--numbers', nargs='*', default=[1, 2.5, 3.0], type=float)

    args = parser.parse_args()

    print(args)
    print(args.numbers)

Advanced parameter parsing
--------------------------
.. code-block:: python

    import argparse


    parser = argparse.ArgumentParser(
        prog='PROGRAM NAME',
        description='A foo that bars',
        epilog="And that's how you'd foo a bar")

    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum,
                        default=max, help='sum the integers (default: find the max)')

    parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('--bar', nargs='+', help='bar help')
    parser.add_argument('--foobar', nargs='*', default=[1, 2, 3], help='BAR!')

    parser.add_argument('--integers', metavar='int',
        type=int, choices=range(10), nargs='+',
        help='an integer in the range 0..9')

    parser.add_argument('--baz', nargs='?', type=int, default=42,
        help='the bar to %(prog)s (default: %(default)s)')

    parser.add_argument('--move', choices=['rock', 'paper', 'scissors'])

    parser.add_argument('--length', default=10, type=int, required=True)
    parser.add_argument('--width', default=10.5, type=float)

    script_arguments = parser.parse_args()
    print(script_arguments)

File handling
-------------
.. code-block:: python

    import argparse


    parser = argparse.ArgumentParser()

    parser.add_argument('--input', default='input.csv', type=argparse.FileType('r'))
    parser.add_argument('--output', default='output.c', type=argparse.FileType('w'))

    args = parser.parse_args()

    with args.input as input, args.output as output:
        content = input.read()
        # do conversion
        output.write(content)


Example
=======
.. code-block:: python

    import argparse
    import sys
    import logging


    def read(filename):
        try:
            with open(filename) as file:
                return file.read()

        except FileNotFoundError:
            logging.critical('File does not exists')
            sys.exit(127)


    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='/tmp/input.csv', type=read)
    args = parser.parse_args()
    print(args)

.. code-block:: python

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='/tmp/input.csv', type=argparse.FileType('r'))

    try:
        args = parser.parse_args()

    except SystemExit:
        print('File does not exists')

    print(args)


``docopt``
==========
* http://docopt.org/
* http://try.docopt.org/
* https://github.com/docopt

.. code-block:: python

    """Naval Fate.

    Usage:
      naval_fate.py ship new <name>...
      naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
      naval_fate.py ship shoot <x> <y>
      naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
      naval_fate.py test (true|false)
      naval_fate.py (-h | --help)
      naval_fate.py --version

    Options:
      -h --help     Show this screen.
      --version     Show version.
      --speed=<kn>  Speed in knots [default: 10].
      --moored      Moored (anchored) mine.
      --drifting    Drifting mine.

    """
    from docopt import docopt


    if __name__ == '__main__':
        arguments = docopt(__doc__, version='Naval Fate 2.0')
        print(arguments)

        test = arguments.get('test', None)
        print(test)

    # python doc.py test on

    # {'--drifting': False,
    #  '--help': False,
    #  '--moored': False,
    #  '--speed': '10',
    #  '--version': False,
    #  '<name>': [],
    #  '<x>': None,
    #  '<y>': None,
    #  'mine': False,
    #  'move': False,
    #  'new': False,
    #  'off': False,
    #  'on': True,
    #  'remove': False,
    #  'set': False,
    #  'ship': False,
    #  'shoot': False,
    #  'test': True}


Assignments
===========

Argument parsing
----------------
#. Napisz parser parametrów linii poleceń
#. Ma przyjmować tylko ``int`` i ``float``
#. Dla parametrów ma uruchomić funkcje ``avg()`` z listingu poniżej:

    .. code-block:: python

        def avg(*args):
            return sum(args) / len(args)

#. Uruchamianie ``python argparse_avg.py --numbers 5 10 100 32 -90 27.5``

:About:
    * Filename: ``argparse_avg.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min
