def is_integer(num):
    """
    >>> is_integer(0)
    True
    >>> is_integer(1)
    True
    >>> is_integer(-1)
    True
    >>> is_integer(1.0)
    True
    >>> is_integer(1.1)
    False
    """
    if num % 1 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    number = input('Podaj liczbę: ')
    wynik = is_integer(number)
    print(wynik)
