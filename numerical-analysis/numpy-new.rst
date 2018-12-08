*****
Numpy
*****


Assgnments
==========


Euclidean distance 2D
---------------------
#. Dany jest ``np.array`` przechowujący wektor
#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są dwuwymiarowe ``(x, y)``
#. Oblicz odległość między nimi
#. Wykorzystaj algorytm Euklidesa
#. Funkcja musi przechodzić ``doctest``

.. literalinclude:: src/math-euclidean-2d.py
    :language: python
    :caption: Euclidean distance 2D

:About:
    * Filename: ``math_euclidean_2d.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 15 min

.. figure:: ../machine-learning/img/k-nearest-neighbors-euclidean-distance.png
    :scale: 100%
    :align: center

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.

Euclidean distance multi dimensions
-----------------------------------
#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są na :math:`N`-wymiarowej przestrzeni ``(x, y, ...)``
#. Punkty :math:`A` i :math:`B` muszą być równo-wymiarowe
#. Funkcja musi przechodzić ``doctest``

.. literalinclude:: src/math-euclidean-ndim.py
    :language: python
    :caption: Euclidean distance N-dimension

:About:
    * Filename: ``math_euclidean_multi_dim.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 15 min
