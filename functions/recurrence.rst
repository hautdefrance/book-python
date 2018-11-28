**********
Recurrence
**********


What is recurrence?
===================
* Also known as recursion
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
