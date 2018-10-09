from typing import Union


def celsius_to_kelvin(celsius: Union[int, float]) -> float:
    """
    >>> celsius_to_kelvin(1)
    274.15
    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(-1)
    272.15
    >>> celsius_to_kelvin(1.5)
    274.65
    >>> celsius_to_kelvin(-300)
    Traceback (most recent call last):
        ...
    ValueError: Temperature in Kelvin cannot be negative
    >>> celsius_to_kelvin('one')
    Traceback (most recent call last):
        ...
    ValueError: Invalid argument
    >>> celsius_to_kelvin([1, 2])
    Traceback (most recent call last):
        ...
    ValueError: Invalid argument
    """
    if not isinstance(celsius, (float, int)):
        raise ValueError('Invalid argument')

    kelvin = celsius + 273.15

    if kelvin < 0:
        raise ValueError('Temperature in Kelvin cannot be negative')

    return kelvin

