***********
Code Smells
***********


Source :cite:`CodeSmells`


#. Using globals - but that is a code smell in any language.
#. Using ``eval`` and ``exec`` unless the input is tightly controlled.
#. Using ``range`` over the ``length`` of a container to iterate over the container, or get the index.
#. Creating a ``list`` of values, when you don’t need to keep the ``list`` - a generator is often better.
#. Having getter and setter methods rather than using properties.
#. Having named methods with similar semantics to existing operators, instead of overriding the magic methods those operators use (eg. having an add method rather than overriding ``__add__()`` and ``__iadd__()`` ) .
#. Using nested loops to combine two iterables rather than using something out of ``itertools``.
#. Having lots of code and classes in a single module rather than having a sensible split of code into well named modules.
#. Unit tests that don’t use mock (or similar).
#. Modules, classes, methods and functions with no ``docstring``
#. Methods and functions which return a value to signify an error rather raising an exception.
#. Using open and similar without using ``with``.
#. Using mutable values as a default arguments value (without a clear comment stating it is deliberate)
#. Using explicit loop to build a ``list``/``set``/``dict`` rather than a comprehension.
#. Using system to call OS commands rather than using ``shutil`` methods.
#. Using ``str`` manipulation (slicing etc) to build file paths rather than use ``os.path`` or ``pathlib``.
#. You code has a function which is a reimplementation of code in the standard library.
#. You have started a new Project in 2019 (or late 2018) which uses Python2, without a good technical reason. It being what you learnt is not a good technical reason - if you learnt Python2 then you can learn Python3.
