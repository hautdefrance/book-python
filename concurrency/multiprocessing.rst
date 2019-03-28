***************
Multiprocessing
***************


Problems
========
* Zakleszczania
* Race Condition


Tworzenie procesów
==================


Synchronizacja procesów
=======================


IPC - Inter-Process Communication
=================================
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
==================

