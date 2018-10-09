def km_na_metry(ile):
    """
    >>> km_na_metry(1)
    1000

    >>> km_na_metry(0)
    0

    >>> km_na_metry(-1)
    Traceback (most recent call last):
        ...
    ValueError

    >>> km_na_metry('adas')
    Traceback (most recent call last):
        ...
    TypeError
    """
    return ile * 1000


if __name__ == "__main__":

    import doctest
    doctest.testmod()
