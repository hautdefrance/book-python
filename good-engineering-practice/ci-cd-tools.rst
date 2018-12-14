***************
Tools for CI/CD
***************


Frontend Testing
================

``selenium``
------------
* http://www.seleniumhq.org/

Selenium automates browsers. That's it! What you do with that power is entirely up to you. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

Selenium 1.0 + WebDriver = Selenium 2.0

- WebDriver is designed in a simpler and more concise programming interface along with addressing some limitations in the Selenium-RC API.
- WebDriver is a compact Object Oriented API when compared to Selenium1.0
- It drives the browser much more effectively and overcomes the limitations of Selenium 1.x which affected our functional test coverage, like the file upload or download, pop-ups and dialogs barrier
- WebDriver overcomes the limitation of Selenium RC's Single Host origin policy

WebDriver is the name of the key interface against which tests should be written in Java, the implementing classes one should use are listed as below:

    - ChromeDriver,
    - EventFiringWebDriver,
    - FirefoxDriver,
    - HtmlUnitDriver,
    - InternetExplorerDriver,
    - PhantomJSDriver,
    - RemoteWebDriver,
    - SafariDriver.


Static Code Analysis
====================

``SonarLint``
-------------
* https://www.sonarlint.org
* Plugin do IDE

``pycodestyle``
---------------
* previously known as ``PEP8``

:About:
    Python style guide checker. ``pycodestyle`` is a tool to check your Python code
    against some of the style conventions in PEP 8.

    * Plugin architecture: Adding new checks is easy.
    * Parseable output: Jump to error location in your editor.
    * Small: Just one Python file, requires only stdlib. You can use just the
    * pep8.py file for this purpose.
    * Comes with a comprehensive test suite.

:Installation:
    .. code-block:: console

        $ pip install pycodestyle

:Usage:
    .. code-block:: console

        $ pycodestyle FILE.py
        $ pycodestyle DIRECTORY/
        $ pycodestyle --statistics -qq DIRECTORY/
        $ pycodestyle --show-source --show-pep8 FILE.py

    .. code-block:: console

        $ python -m pycodestyle FILE.py

:Config:
    ``setup.cfg``

    .. code-block:: ini

        [pycodestyle]
        max-line-length = 939
        ignore = E402,W391
        exclude = */migrations/*

``flake8``
----------
:About:
    Simply speaking flake8 is "the wrapper which verifies ``pycodestyle``, ``pyflakes`` and circular complexity". For other functions, it can control the warnings for specific line (impossible by a simple pyflakes)by # flake8: noqa or it can customize warnings happening by configuration file such as ``pycodestyle``.

``SonarQube``
-------------

:About:
    SonarQube software (previously called Sonar) is an open source quality management platform, dedicated to continuously analyze and measure technical quality, from project portfolio to method.

:More information:
    * https://sonarqube.com
    * http://docs.sonarqube.org/display/SONAR/Documentation
    * https://sonarqube.com/dashboard/index?did=143
    * https://sonarqube.com/governance?id=662857


``Pylint``
----------

:About:
    Pylint is a Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells (as defined in Martin Fowler’s Refactoring book). Pylint has many rules enabled by default, way too much to silence them all on a minimally sized program. It’s highly configurable and handle pragmas to control it from within your code. Additionally, it is possible to write plugins to add your own checks.

    Coding Standard:

    - checking line-code's length,
    - checking if variable names are well-formed according to your coding standard
    - checking if imported modules are used

    Error detection:

    - checking if declared interfaces are truly implemented
    - checking if modules are imported and much more (see the complete check list)

    Pylint is shipped with Pyreverse which creates UML diagrams for python code.

:Install:
    .. code-block:: console

        $ pip install pylint

:Usage:
    .. code-block:: console

        $ pylint DIRECTORY/
        $ pylint FILE.py

:More information:
    * https://pypi.python.org/pypi/pylint/


``Pyflakes``
------------

:About:
    A simple program which checks Python source files for errors. Pyflakes analyzes programs and detects various errors. It works by parsing the source file, not importing it, so it is safe to use on modules with side effects. It’s also much faster.

:Install:
    .. code-block:: console

        $ pip install pyflakes

:Usage:
    .. code-block:: console

        $ pyflakes DIRECTORY/
        $ python -m pyflakes DIRECTORY/

:More information:
    * https://pypi.python.org/pypi/pyflakes


``Coverage``
------------

:About:
    Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.

:Install:
    .. code-block:: console

        $ pip install coverage

:Usage:
    .. code-block:: console

        $ coverage run FILE.py
        $ coverage report -m

    Use coverage run to run your program and gather data:

    .. code-block:: console

        $ coverage run my_program.py arg1 arg2
        blah blah ..your program's output.. blah blah

    Use coverage report to report on the results:

    .. code-block:: console

        $ coverage report -m
        Name                      Stmts   Miss  Cover   Missing
        -------------------------------------------------------
        my_program.py                20      4    80%   33-35, 39
        my_other_module.py           56      6    89%   17-23
        -------------------------------------------------------
        TOTAL                        76     10    87%

    For a nicer presentation, use ``coverage html`` to get annotated HTML listings detailing missed lines:

    .. code-block:: console

        $ coverage html


:More information:
    * https://pypi.python.org/pypi/coverage
    * https://coverage.readthedocs.io/

Behavioral Testing
==================

``behave``
----------
* https://github.com/behave/behave

FILE: features/example.feature

    .. code-block:: text

        Feature: Showing off behave

          Scenario: Run a simple test
            Given we have behave installed
             When we implement 5 tests
             Then behave will test them for us!

FILE: features/steps/example_steps.py:

    .. code-block:: python

        from behave import given, when, then, step

        @given('we have behave installed')
        def step_impl(context):
            pass

        @when('we implement {number:d} tests')
        def step_impl(context, number):  # -- NOTE: number is converted into integer
            assert number > 1 or number == 0
            context.tests_count = number

        @then('behave will test them for us!')
        def step_impl(context):
            assert context.failed is False
            assert context.tests_count >= 0

Output:
    .. code-block:: console

        $ behave
        Feature: Showing off behave # features/example.feature:2

          Scenario: Run a simple test          # features/example.feature:4
            Given we have behave installed     # features/steps/example_steps.py:4
            When we implement 5 tests          # features/steps/example_steps.py:8
            Then behave will test them for us! # features/steps/example_steps.py:13

        1 feature passed, 0 failed, 0 skipped
        1 scenario passed, 0 failed, 0 skipped
        3 steps passed, 0 failed, 0 skipped, 0 undefined

Type Checking
=============

``mypy`` type checking
----------------------
* http://mypy-lang.org/
* https://github.com/python/mypy

.. code-block:: console

    $ pip install mypy
    $ mypy FILE

``setup.cfg``

.. code-block:: ini

    [mypy]
    strict_optional = True

``pyre-check``
--------------
* https://pyre-check.org/

.. code-block:: console

    $ pip install pyre-check

Automation and Releases
=======================

Fabric
------

:Install:
    .. code-block:: console

        $ pip install fabric

PSSH
----

Testy Mutacyjne
===============

* https://pypi.python.org/pypi/MutPy
* https://pypi.python.org/pypi/MutPy/0.4.0
* https://github.com/sixty-north/cosmic-ray
* https://hackernoon.com/mutmut-a-python-mutation-testing-system-9b9639356c78
* https://www.youtube.com/watch?v=jwB3Nn4hR1o
* http://cosmic-ray.readthedocs.io/en/latest/
* https://github.com/sk-/elcap

Translation
===========

Transifex
---------
* https://www.transifex.com

PoEdit
------
