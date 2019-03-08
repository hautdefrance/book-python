*******
Doctest
*******


* używane jako zawsze aktualna dokumentacja kodu
* sprawdzają poprawność działania funkcji
* niezwykle przydatne przy tworzeniu regexpów
* można przetykać tekst pomiędzy testami

Running tests
=============

Running tests with your IDE
---------------------------

From command line
-----------------
* Without ``-v`` this won’t display anything unless an example fails

.. code-block:: console

    python -m doctest -v example.py

From code
---------
.. code-block:: python

    if __name__ == "__main__":
        import doctest
        doctest.testmod()


Test for ``bool`` return values
===============================
.. code-block:: python

    AGE_ADULT = 18

    def is_adult(age):
        """
        Function checks if person is adult.
        Adult person is over 18 years old.

        >>> is_adult(18)
        True

        >>> is_adult(17.9)
        False
        """
        if age >= AGE_ADULT:
            return True
        else:
            return False


Test for ``int`` return values
==============================
.. code-block:: python

    def add(a, b):
        """
        Function adds two numbers

        >>> add(1, 2)
        3

        >>> add(-1, 1)
        0

        >>> add(0, 0)
        0
        """
        return a + b


Test for ``str`` return values
==============================

Returning ``str``
-----------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        Function returns the name of the astronaut
        >>> hello('Иван Иванович')
        'Иван Иванович'

        Default value is 'José Jiménez'
        >>> hello()
        'José Jiménez'
        """
        return name

Printing ``str``
----------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        Function prints on the screen the name of the astronaut
        >>> hello('Иван Иванович')
        Иван Иванович

        Default value is 'José Jiménez'
        >>> hello()
        José Jiménez
        """
        print(name)

Printing ``str`` with newlines
------------------------------
.. code-block:: python

    def hello(name='José Jiménez'):
        """
        Greet's an astronaut.
        Last line is blank.

        >>> hello()
        José Jiménez
        José Jiménez
        José Jiménez
        <BLANKLINE>
        """
        print(f'{name}\n' * 3)

Testing for exceptions
======================
.. code-block:: python

    def add(a, b):
        """
        Function adds two numbers.
        It checks for proper type of input.

        >>> add(1, 2)
        3

        >>> add(-1, 1)
        0

        >>> add(0, 0)
        0

        Function should do:
            - one thing
            - one thing only
            - one thing good

        Adding list elements is not a business of this function.

        >>> add([1, 2])
        Traceback (most recent call last):
            ...
        TypeError: Argument must be int or float
        """
        if not isinstance(a, (int, float)):
            raise TypeError('Argument must be int or float')

        if not isinstance(b, (int, float)):
            raise TypeError('Argument must be int or float')

        return a + b


Using python statements in ``doctest``
======================================
.. code-block:: python

    def when(date):
        """
        >>> from datetime import datetime, timezone
        >>> moon = datetime(1969, 7, 21, 17, 54, tzinfo=timezone.utc)
        >>> hello(moon)
        '1969-07-21 17:54 UTC'
        """
        print(f'{date:%Y-%m-%d %H:%M %Z}')


Running doctest from standalone scripts
=======================================
* Testy dla wszystkich funkcji aktualnie zdefiniowanych w przestrzeni nazw

.. literalinclude:: src/doctest-testmod.py
    :language: python
    :caption: Wykorzystanie ``doctest.testmod()`` do uruchamiania testów


Practical example
=================

Celsius to Kelvin temperature conversion
----------------------------------------
.. literalinclude:: src/doctest-corner-cases.py
    :language: python
    :caption: Pokrycie przypadków brzegowych doctestami


Email regex
-----------
.. code-block:: python

    import re

    VALID_EMAIL = r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'


    def is_valid_email(email: str) -> bool:
        """
        Function check email address against Regular Expression

        >>> is_valid_email('jose.jimenez@nasa.gov')
        True

        >>> is_valid_email('Jose.Jimenez@nasa.gov')
        True

        >>> is_valid_email('+jose.jimenez@nasa.gov')
        False

        >>> is_valid_email('jose.jimenez+@nasa.gov')
        True

        >>> is_valid_email('jose.jimenez+newsletter@nasa.gov')
        True

        >>> is_valid_email('jose.jimenez@.gov')
        False

        >>> is_valid_email('@nasa.gov')
        False

        >>> is_valid_email('jose.jimenez@nasa.g')
        False
        """
        if re.match(VALID_EMAIL, email):
            return True
        else:
            return False

URL Regex
---------
.. code-block:: python

    # @diegoperini --  https://mathiasbynens.be/demo/url-regex
    REGEX = r'_^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$_iuS'

    def is_valid_url(url):
        if re.match(REGEX, url):
            return True
        else:
            return False

Assignments
===========

Refactoring
-----------
* Filename: ``doctest_temp.py``
* Lines of code to write: 5 lines of code
* Estimated time of completion: 15 min

#. Dana jest funkcja ``celsius_to_kelvin(degrees)``
#. Napisz ciało funkcji aby testy przechodziły:

    .. code-block:: python

        def celsius_to_kelvin(degrees):
            """
            >>> celsius_to_kelvin(0)
            273.15
            >>> celsius_to_kelvin(1)
            274.15
            >>> celsius_to_kelvin(-1)
            272.15
            >>> celsius_to_kelvin('a')
            Traceback (most recent call last):
                ...
            TypeError: Invalid argument
            >>> celsius_to_kelvin([0, 1])
            [273.15, 274.15]
            >>> celsius_to_kelvin((0, 1))
            (273.15, 274.15)
            >>> celsius_to_kelvin({0, 1})
            {273.15, 274.15}
            """
            pass

Distance conversion doctest
---------------------------
* Filename: ``doctest_distance.py``
* Lines of code to write: 5 lines of code + 16 lines of tests
* Estimated time of completion: 10 min

#. Napisz funkcję, która przeliczy dystans podany w metrach na kilometry
#. 1 km = 1000 m
#. Dystans nie może być ujemny
#. Zwracany dystans musi być zawsze float
#. Napisz testy do rozwiązania i pokryj przypadki:

    * dystans w metrach jest -1 (ujemny)
    * dystans w metrach jest 0 (zero)
    * dystans w metrach jest 1 (dodatni)
    * dystans w metrach jest ``float``
    * dystans w metrach jest ``int``
    * podano listę odległości
    * podany parametr to ``str``

Fix URL Regex
-------------
* Lines of code to write: 0 lines
* Estimated time of completion: 5 min

#. Dane jest wyrażenie z listingu poniżej

    .. code-block:: python

        REGEX = r'_^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$_iuS'

#. Wyrażenie niepoprawnie klasyfikuje adres 'https://foo_bar.example.com/'
#. Popraw wyrażenie nie psując parsowania wszystkich pozostałych przypadków
#. Poprawne URL:

    .. code-block:: text

        http://foo.com/blah_blah
        http://foo.com/blah_blah/
        http://foo.com/blah_blah_(wikipedia)
        http://foo.com/blah_blah_(wikipedia)_(again)
        http://www.example.com/wpstyle/?p=364
        https://www.example.com/foo/?bar=baz&inga=42&quux
        http://✪df.ws/123
        http://userid:password@example.com:8080
        http://userid:password@example.com:8080/
        http://userid@example.com
        http://userid@example.com/
        http://userid@example.com:8080
        http://userid@example.com:8080/
        http://userid:password@example.com
        http://userid:password@example.com/
        http://142.42.1.1/
        http://142.42.1.1:8080/
        http://➡.ws/䨹
        http://⌘.ws
        http://⌘.ws/
        http://foo.com/blah_(wikipedia)#cite-1
        http://foo.com/blah_(wikipedia)_blah#cite-1
        http://foo.com/unicode_(✪)_in_parens
        http://foo.com/(something)?after=parens
        http://☺.damowmow.com/
        http://code.google.com/events/#&product=browser
        http://j.mp
        ftp://foo.bar/baz
        http://foo.bar/?q=Test%20URL-encoded%20stuff
        http://مثال.إختبار
        http://例子.测试
        http://उदाहरण.परीक्षा
        http://-.~_!$&'()*+,;=:%40:80%2f::::::@example.com
        http://1337.net
        http://a.b-c.de
        http://223.255.255.254
        https://foo_bar.example.com/

#. Niepoprawne url:

    .. code-block:: text

        http://
        http://.
        http://..
        http://../
        http://?
        http://??
        http://??/
        http://#
        http://##
        http://##/
        http://foo.bar?q=Spaces
        //
        //a
        ///a
        ///
        http:///a
        foo.com
        rdar://1234
        h://test
        http:// shouldfail.com
        :// should fail
        http://foo.bar/foo(bar)baz quux
        ftps://foo.bar/
        http://-error-.invalid/
        http://a.b--c.de/
        http://-a.b.co
        http://a.b-.co
        http://0.0.0.0
        http://10.1.1.0
        http://10.1.1.255
        http://224.1.1.1
        http://1.1.1.1.1
        http://123.123.123
        http://3628126748
        http://.www.foo.bar/
        http://www.foo.bar./
        http://.www.foo.bar./
        http://10.1.1.1
        http://10.1.1.254
