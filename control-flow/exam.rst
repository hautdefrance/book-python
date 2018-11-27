**********************
Exam from basic topics
**********************

Parsowanie ``/etc/passwd``
--------------------------
#. Poniższe listingi prezentują zawartość plików:

    - ``/etc/passwd`` - :numref:`code-file-etc-passwd`
    - ``/etc/shadow`` - :numref:`code-file-etc-shadow`
    - ``/etc/group`` - :numref:`code-file-etc-group`

#. Skopuj ich zawartość każdego z tych plików na dysk (uwaga: komentarze i puste mają również być skopiowane)
#. Sparsuj plik i przedstaw go w formacie ``List[dict]``
#. Zwróć listę użytkowników, których UID jest większy niż 1000
#. W ramach dicta połącz dane, tak aby uzyskać wynik:

    .. code-block:: python

        [
            {
                'login': 'jimenez',
                'uid': 1001,
                'gid': 1001,
                'home': '/home/jimenez',
                'shell': '/bin/bash',
                'algorithm': 'SHA-512',
                'password': 'P9zn0KwR...k4kijuhE50',
                'groups': ['staff', 'sysadmin'],
                'last_changed': datetime.date(2015, 7, 16),
                'locked': False,
            },
            ...
        ]

:About:
    * Filename: ``exam-foundations.py``
    * Lines of code to write: 60 lines
    * Estimated time of completion: 60 min

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * łączenie danych z różnych plików w jeden format wynikowy
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym
    * różna reprezentacja danych (podmienianie wartości)

.. literalinclude:: src/etc-passwd.txt
    :name: code-file-etc-passwd
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/passwd``

.. literalinclude:: src/etc-shadow.txt
    :name: code-file-etc-shadow
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/shadow``

.. literalinclude:: src/etc-group.txt
    :name: code-file-etc-group
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/group``
