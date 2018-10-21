.. _Advanced Functions:

******************
Advanced Functions
******************


Type annotations
================
* Od Python 3.5
* Kod w języku python wykona się nawet jeśli typ nie zgadza się z adnotacją!
* Twoje IDE porówna typy oraz poinformuje cię jeżeli wykryje niezgodność
* Użyj ``mypy`` lub ``pyre-check`` do sprawdzania typów

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add(1, 2.5)
    # 3.5

.. code-block:: python

    def add(a: int, b: float) -> float:
        return a + b

    add('José', 'Jiménez')
    # 'JoséJiménez'

.. note:: więcej na ten temat w rozdziale dotyczącym :ref:`Type Annotation`


Recurrence
==========
* Aby zrozumieć rekurencję – musisz najpierw zrozumieć rekurencję
* Maksymalny limit rekurencji = 1000
* Zmiana limitu ``sys.setrecursionlimit(limit)``
* CPython implementation doesn't optimize tail recursion, and unbridled recursion causes stack overflows.
* Python isn't a functional language and tail recursion is not a particularly efficient technique
* Rewriting the algorithm iteratively, if possible, is generally a better idea.

.. code-block:: python

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


Callable
========
.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    hello                 # <function hello at 0x0C55D420>
    type(hello)           # <class 'function'>
    hello()               # My name... José Jiménez

.. code-block:: python

    'hello'               # 'hello'
    type('hello')         # <class 'str'>
    'hello'()             # TypeError: 'str' object is not callable

Returning function (callable)
-----------------------------
.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    def function():
        return hello

    my_name = function()  # <function __main__.hello()>
    my_name()             # My name... José Jiménez

.. code-block:: python

    import datetime
    import time

    now = datetime.datetime.now()

    print(now)            # 1969-07-21 14:56:15
    time.sleep(10)
    print(now)            # 1969-07-21 14:56:15

.. code-block:: python

    import datetime
    import time

    now = datetime.datetime.now

    print(now())          # 1969-07-21 14:56:15
    time.sleep(10)
    print(now())          # 1969-07-21 14:56:25


Operator ``*`` i ``**``
=======================
- ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
- ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane

Przypomnienie wiadomości o parametrach
--------------------------------------
.. code-block:: python

    def add(a, b):
        return a + b


    add(1, 2)       # pozycyjne
    add(a=1, b=2)   # nazwane, kolejność nie ma znaczenia
    add(b=2, a=1)   # nazwane, kolejność nie ma znaczenia

.. code-block:: python

    a, b = 1, 2
    a, b = (1, 2)
    a, b = [1, 2]

.. code-block:: python

    def numbers():
        return 1, 2

    a, b = numbers()

Przyjmowanie z funkcji zmiennej ilości argumentów
-------------------------------------------------
.. code-block:: python

    line = 'jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash'
    line.split(':')
    # ['jimenez', 'x', '1001', '1001', 'José Jiménez', '/home/jimenez', '/bin/bash']

.. code-block:: python

    username, password, uid, gid, name, home, shell = line.split(':')
    username    # jimenez
    password    # x

.. code-block:: python

    username, password, *others = line.split(':')
    username    # jimenez
    password    # x
    others      # ['1001', '1001', 'José Jiménez', '/home/jimenez', '/bin/bash']

.. code-block:: python

    *others, home, shell = line.split(':')
    others      # ['jimenez', 'x', '1001', '1001', 'José Jiménez']
    home        # '/home/jimenez'
    shell       # '/bin/bash'

.. code-block:: python

    *a, b, *c = [1, 2, 3, 4, 5, 6, 7]
    # SyntaxError: two starred expressions in assignment

.. code-block:: python

    # if you're not using ``others`` later in your code
    username, *_ = line.split(':')

.. code-block:: python

    class Point:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def get_position(self):
            return self.x, self.y, self.z

    p = Point(10, 20)
    p.get_position()    # 10, 20
    x, y, z = p.get_position()
    x, *_ = p.get_position()

.. code-block:: python

    def sensor_temperatury():
        # ładniej byłoby gdyby programista napisał
        # {'napiecie': 10, 'natezenie': 20, 'rezystancja': 30, 'czas': 5, 'location': 'laboratorium'}
        # ale programiści niskopoziomowi zwykle zwracają jako list...
        return (10, 20.6, 30, 5, 'laboratorium')

    napiecie, natezenie, *_ = sensor_temperatury()

Definiowanie funkcji ze zmienną ilością parametrów
--------------------------------------------------
- ``args`` - pozycyjne
- ``kwargs``- nazwane

.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *pozycyjne, **nazwane):
        print(f'argument a: {a}')                   # 1
        print(f'argument b: {b}')                   # 2
        print(f'argument c: {c}')                   # 3
        print(f'argumenty pozycyjne: {pozycyjne}')  # 4, 5, 6
        print(f'argumenty nazwane: {nazwane}')      # d=7, e=8


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=7, e=8)

.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *args, **kwargs):
        print(f'argument a: {a}')                   # 1
        print(f'argument b: {b}')                   # 2
        print(f'argument c: {c}')                   # 3
        print(f'argumenty args: {args}')            # 4, 5, 6
        print(f'argumenty kwargs: {kwargs}')        # d=7, e=8


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=7, e=8)

Kiedy to się przydaje:

.. code-block:: python

    def celsius_to_fahrenheit(*degrees):
        return [degree*1.8+32 for degree in degrees]

    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]

Przekazywanie do funkcji zmiennej ilości parametrów
---------------------------------------------------
Przykładowe zastosownaie operatorów ``*`` i ``**`` polega na wykorzystaniu ich przy wywołaniu funkcji. Wtedy, wykorzystując operator ``*``, kolejne elementy listy albo krotki będą przekazane jako kolejne argumenty funkcji, a wykorzystując operator ``**`` kolejne elementy zmiennej słownikowej będą przekazane jako nazwane argumenty. Oznacza to, że na przykład argument ``x`` funkcji, przyjmie wartość ``vector['x']``.

.. code-block:: python

    def my_function(x, y, z):
        print(x, y, z)

    vector = (1, 0, 1)
    my_function(*vector)   # my_function(1, 0, 1)
    # 1, 0, 1

    vector = {'y': 1, 'x': 0, 'z': 1}
    my_function(**vector)  # my_function(y=1, x=0, z=1)
    # 0, 1, 1

.. code-block:: python

    def wyswietl(a, b, c=0):
        print(locals())

    wyswietl(1, 2, 3)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2, 3)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 0}

.. code-block:: python

    def wyswietl(a, b, c=0, *args):
        print(locals())

    dane = (1, 2, 3, 4)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4,)}

    dane = (1, 2, 3, 4, 5, 6, 7)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6, 7)}

    wyswietl(1, 2)
    # {'a': 1, 'b': 2, 'c': 0, 'args': ()}

.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    wyswietl(1, 2, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 0, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    wyswietl(1, 2, x=77, y=99, c=7)
    # {'a': 1, 'b': 2, 'c': 7, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    dane = {'x': 77, 'y': 99}
    wyswietl(1, 2, 3, **dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    dane = {'a': 1, 'b': 2, 'x': 77, 'y': 99}
    wyswietl(**dane)
    # {'a': 1, 'b': 2, 'c': 0, 'args': (), 'kwargs': {'x': 77, 'y': 99}}


.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    dane = {'x': 77, 'y': 99, 'a': 7}
    wyswietl(1, 2, 3, **dane)
    # TypeError: wyswietl() got multiple values for argument 'a'

.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    wyswietl(1, 2, 3, 4, 5, 6, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}

    pozycyjne = (4, 5, 6)
    nazwane = {'x': 77, 'y': 99}
    wyswietl(1, 2, 3, *pozycyjne, **nazwane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}

Przykładowe zastosowanie
========================
.. code-block:: python

    from typing import List

    def celsius_to_fahrenheit(*degrees) -> List[float]:
        return [x * 1.8 + 32 for x in degrees]


    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]

.. code-block:: python

    class Kontakt:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    Kontakt(imie='Matt', nazwisko='Kowalski')

.. code-block:: python

    class Osoba:
        first_name = 'Matt'
        last_name = 'Kowalski'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)
            return '{first_name} {last_name}'.format(first_name='Matt', last_name='Kowalski')
            return f'{self.first_name} {self.last_name}'

.. code-block:: python

    def wyswietl(*args, **kwargs):
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

    def function(a, b, c=0):
        x = 4
        y = 5

        wyswietl(**locals())

    function(1, 2)
    # args: ()
    # kwargs: {'a': 1, 'b': 2, 'c': 0, 'x': 4, 'y': 5}


Assignments
===========

Iris
----
#. Otwórz link w przeglądarce https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv i skopiuj jego zawartość do pliku ``dataset-iris.csv`` na dysku
#. Sparsuj zawartość odrzucając nagłówek
#. Stwórz funkcję ``print_iris(*args, **kwargs)``, która wyświetli zawartość ``args`` i ``kwargs``
#. Dla każdego rekordu odpalaj funkcję, podając wartości korzystając z operatora ``*``


Hosts
-----
#. Skopiuj zawartość listingu :numref:`listing-etc-hosts` do pliku ``hosts.txt``
#. Stwórz pusty ``dict`` o nazwie ``hosts``
#. Czytając plik pomiń puste linie lub zaczynające się od komentarza ``#``
#. Do ``hosts`` dla klucza IP dodaj listę hostname
#. Przy parsowaniu linii skorzystaj z konstrukcji z gwiazdką ``*``

:About:
    * Filename: ``functions_hosts.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 15 min

.. literalinclude:: src/etc-hosts.txt
    :name: listing-etc-hosts
    :language: python
    :caption: Listing pliku ``/etc/hosts``

Deserialize
-----------
#. Po API dostajesz JSONa tak jak na listingu poniżej
#. Iterując po rekordach twórz obiekty klasy ``Astronaut``
#. Sparsuj ``user_permissions`` i przedstaw je za pomocą listy klas
#. Nazwa klasy to klucz w słowniku
#. Są zawsze cztery pola: ``"add", "modify", "view", "delete"``
#. Jeżeli jakieś pole jest wymienione, to ma wartość ``True``, jeżeli nie to ``False``

.. code-block:: text

    [{"model":"authorization.user","pk":1,"fields":{"password":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqvXNiCeTrY0CRSLYYAA90=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"commander","first_name":"Иван","last_name":"Иванович","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","last_login":null,"is_superuser":false,"username":"executive-officer","first_name":"José","last_name":"Jiménez","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"eclss":["add","modify","view"]},{"communication":["add","modify","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":3,"fields":{"password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb62WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","last_login":"1970-01-01T00:00:00.000Z","is_superuser":false,"username":"crew-medical-officer","first_name":"Melissa","last_name":"Lewis","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"medical":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":4,"fields":{"password":"pbkdf2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTrYYZ3sB1r0g=","last_login":null,"is_superuser":false,"username":"science-data-officer","first_name":"Mark","last_name":"Watney","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":5,"fields":{"password":"pbkdf2_sha256$120000$bxS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","last_login":null,"is_superuser":false,"username":"communication-officer","first_name":"Matt","last_name":"Kowalski","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","modify","view"]},{"science":["add","modify","view"]}]}},{"model":"authorization.user","pk":6,"fields":{"password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/qhXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","last_login":null,"is_superuser":false,"username":"eclss-officer","first_name":"Harry","last_name":"Stamper","email":"","is_staff":true,"is_active":true,"date_joined":"1970-01-01T00:00:00.000Z","groups":[1],"user_permissions":[{"communication":["add","view"]},{"eclss":["add","modify","view"]},{"science":["add","modify","view"]}]}}]
