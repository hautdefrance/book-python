def factorial(n):
    if not hasattr(factorial, '__cache__'):
        factorial.__cache__ = {1: 1}

    if not n in factorial.__cache__:
        factorial.__cache__[n] = n * factorial(n - 1)

    return factorial.__cache__[n]
