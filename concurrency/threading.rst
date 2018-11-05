*****************************
Queues, Threads and Processes
*****************************


Kolejki - Queue
===============

FIFO
----

LIFO (stack)
------------

Network Queue
-------------
* Synchronizacja
* Routing

Priority Queue
--------------
* Priorytetyzacja
* Wywłaszczenie


Threads vs processes
====================
* Czym się różnią wątki od procesów?
* Ile wątków może być w ramach procesów?
* Jak komunikować się między wątkami?
* Jak komunikować się między procesami?
* Ile może być wątków na procesorze czterordzeniowym (z i bez Hyper Threading)?
* Ile może być procesów na procesorze czterordzeniowym (z i bez Hyper Threading)?
* Czy współdzielenie pamięci przez wątki jest dobre czy złe?


Threads
=======

Problemy z wątkami
--------------------
- Zakleszczania
- Race Condition
- Głodzenie
- Problem 5 filozofów:

    - 5 filozofów (albo rozmyśla, albo je)
    - 5 misek ze spagetti,
    - 5 widelców,
    - 2 widelce potrzebne aby zjeść,
    - problem zakleszczania

- Problem producenta i konsumenta
- Problem czytelników i pisarzy

Tworzenie wątków
----------------
* dlaczego nie ``time.sleep()``
* rekurencyjny timer

.. literalinclude:: src/threading-timer.py
    :name: listing-threading-timer
    :language: python
    :caption: Timer

Synchronizacja wątków
---------------------
.. literalinclude:: src/threading-synchronization.py
    :name: listing-threading-synchronization
    :language: python
    :caption: Synchronizacja wątków

Zamykanie wątków
----------------


Workery
-------
.. literalinclude:: src/threading-worker.py
    :name: listing-threading-worker
    :language: python
    :caption: Model Workerów


Processes
=========

Problemy z procesami
--------------------
* Zakleszczania
* Race Condition

Tworzenie procesów
------------------

Synchronizacja procesów
-----------------------

IPC - komunikacja międzyprocesowa
---------------------------------
Aby ``pickle`` mógł odtworzyć obiekt, musi posiadać jego definicję - klasę.

.. literalinclude:: src/figury.py
    :name: listing-figury
    :language: python
    :caption: Klasa Prostokat w module figury

.. literalinclude:: src/multiprocessing-client.py
    :name: listing-multiprocessing-client
    :language: python
    :caption: Obiekt wysyłający dane ``multiprocessing-client.py``

.. literalinclude:: src/multiprocessing-listener.py
    :name: listing-multiprocessing-listener
    :language: python
    :caption: Obiekt nasłuchujący na połączenia ``multiprocessing-listener.py``


Zamykanie procesów
------------------


Assignments
===========

Wielowątkowość
--------------
#. Stwórz kolejkę ``queue`` do której dodasz różne polecenia systemowe do wykonania, np.:

    - Lunux/macOS: ``['/bin/ls /etc/', '/bin/echo "test"', '/bin/sleep 2']``,
    - Windows: ``['dir c:\\Users', 'echo "test"', 'type %HOMEPATH%\Desktop\README.txt']``.

#. Parametry rozbij za pomocą ``shlex``
#. Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki.
#. Wątki powinny być uruchamiane jako ``subprocess.run()`` w systemie operacyjnym z timeoutem równym ``PROCESSING_TIMEOUT = 2.0`` sekundy
#. Ilość poleceń może się zwiększać w miarę wykonywania zadania.
#. Wątki powinny być uśpione za pomocą ``Timer`` przez 5.0 sekund, a następnie ruszyć do roboty.
#. Wątki mają być uruchomione w tle (ang. ``daemon``)
#. Użyj logowania za pomocą biblioteki ``logging`` tak aby przy wyświetlaniu wyników widoczny był identyfikator procesu i wątku.

:About:
    * Filename: ``multiprocessing_server.py`` i ``multiprocessing_client.py``
    * Lines of code to write: 50 lines
    * Estimated time of completion: 30 min
