.. _Builtin and Keywords:

********************
Builtin and Keywords
********************


Keywords
========

``pass``
--------
Python domyślnie oczekuje wcięcia po dwukropku. Jeżeli chcemy zostawić klasę czy funkcję pustą, korzystamy wtedy ze słowa kluczowego ``pass``.

.. code-block:: python

    def my_function():
        pass

.. code-block:: python

    def my_function():
        pass

    my_var = my_function()
    # None

``__file__``
------------
.. code-block:: python

    import os

    BASE_DIR = os.path.dirname(__file__)
    path = os.path.join(BASE_DIR, 'main.py')

``__name__``
------------
* Zmienna ``__name__`` pozwala ustalić czy dany plik jest wykonywany czy importowany.
* Jeżeli dany plik jest wykonywany, zmienna ``__name__`` ustawiana jest na ``'__main__'``.
* Jeżeli dany plik jest importowany jako moduł, zmienna ``__name__`` ustawiana jest na nazwę modułu.
* Jest to przydatne na przykład przy testowaniu modułów.

Dodanie do modułu poniższej linijki:

.. code-block:: python

    if __name__ == '__main__':
        print('hello world')

Sprawi, że wypisane na konsoli zostanie ``'hello world!'`` jeżeli dany plik jest uruchamiany z konsoli. Powyższy kod nie wykona się natomiast jeżeli plik zaimportujemy jako moduł w innym pliku.

Przykład z życia:

.. code-block:: python

    import logging

    log = logging.getLogger(__name__)

.. code-block:: python

    def run():
        ...

    if __name__ == '__main__':
        # Jeżeli skrypt wywoływany jest z konsoli "z ręki" to uruchom funckję ``run()``
        # Jeżeli został zaimportowany, to ten fragment będzie zignorowany
        # I trzeba uruchomić funkcję ``run()`` samodzielnie - kontrolowanie
        run()


Builtin functions
=================

``range()``
-----------
* Tworzy **iterator**, który zwraca liczby w sekwencji.

.. code-block:: python

    for liczba in range(0, 5):
        print(liczba)


    for liczba in range(0, 5, 2):
        print(liczba)

.. code-block:: python

    numbers_generator = range(0, 5)
    print(numbers_generator)
    # range(0, 5)

.. code-block:: python

    numbers_generator = range(0, 5)
    numbers = list(numbers_generator)

    print(numbers)  # [0, 1, 2, 3, 4]

``isinstance()``
----------------
* Sprawdza czy dany obiekt jest instancją danej klasy
* Jeżeli jest więcej niż jeden typ to musi być ``tuple`` a nie ``list`` lub ``set``

.. code-block:: python

    isinstance(10, int)           # True
    isinstance(10, float)         # False
    isinstance(10, (int, float))  # True

``bin()``
---------
* Konwertuje liczbę na binarną
* Nie stosuje kodu uzupełnień do dwóch

.. code-block:: python

    0b101111    # 47

.. code-block:: python

    bin(3)      # '0b11'
    bin(-3)     # '-0b11'

``hex()``
---------
* Konwertuje liczbę na heksadecymalną
* Konwersja kolorów w HTML
* Shellcode

.. code-block:: python

    hex(99)  # '0x63'

``oct()``
---------
* Konwertuje liczbę na octalną
* Przydatne do uprawnień w systemie operacyjnym

.. code-block:: python

    oct(33261)  # '0o100755'

``ord()``
---------
Zwraca kod ASCII jednoznakowego stringa.

.. code-block:: python

    ord('a')  # 97

``chr()``
---------
Z pozycji w tablicy ASCII konwertuje kod na znak Unicode.

.. code-block:: python

    chr(97)  # 'a'

``eval()``
----------
.. code-block:: python

    eval('name="José Jiménez"; print(name)')
    # José Jiménez


Other builtin functions
=======================
.. csv-table:: Most used Built-in functions
    :header-rows: 1
    :file: data/builtins.csv


Assignments
===========

Average
-------
* Filename: ``builtin_average.py``
* Lines of code to write: 12 lines
* Estimated time of completion: 15 min

#. Dane są pomiary Irysów:

    .. literalinclude:: assignments/builtin-iris-sample.py
        :language: python
        :caption: Sample Iris databases

#. Na podstawie nagłówka stwórz ``dict`` z pustymi ``list`` dla każdego z parametrów"

    .. code-block:: python

        values = {
            'Sepal length': [],
            'Sepal width': [],
            'Petal length': [],
            'Petal width': [],
            'Species': [],
        }

#. Stwórz funkcję ``average()``, która będzie liczyła średnią dla dowolnej ilości argumentów

    .. code-block:: python

        def average(args: List[float]) -> float:
            pass

#. Do wyliczenia średniej, wykorzystaj wbudowane funkcje
#. Funkcja ma wyliczać średnią tylko dla parametrów typu ``float``, w przeciwnym wypadku zwróć ``None``
#. Do ``averages: Dict[str, float]`` wpisz wyliczone wartości dla każdego z parametrów

    .. code-block:: python

        averages = {
            'Sepal length': average(...),
            'Sepal width': average(...),
            'Petal length': average(...),
            'Petal width': average(...),
            'Species': average(...),
        }

#. Wypisz na ekranie ``values`` oraz ``averages``

:The whys and wherefores:
    * Korzystanie z funkcji wbudowanych
    * Iterowanie po kolekcji
    * Wybieranie rekordów

