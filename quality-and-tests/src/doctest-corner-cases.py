from typing import Union


def celsius_to_kelvin(temperature_in_celsius: Union[int, float]) -> float:
    """
    >>> celsius_to_kelvin(0)
    273.15

    >>> celsius_to_kelvin(1)
    274.15

    >>> celsius_to_kelvin(-1)
    272.15

    >>> celsius_to_kelvin(-273.15)
    0.0

    >>> celsius_to_kelvin(-274.15)
    Traceback (most recent call last):
        ...
    ValueError: Argument must be greater than -273.15

    >>> celsius_to_kelvin([-1, 0, 1])
    Traceback (most recent call last):
        ...
    ValueError: Argument must be int or float

    >>> celsius_to_kelvin('one')
    Traceback (most recent call last):
        ...
    ValueError: Argument must be int or float
    """
    if not isinstance(temperature_in_celsius, (float, int)):
        raise ValueError('Argument must be int or float')

    if temperature_in_celsius < -273.15:
        raise ValueError('Argument must be greater than -273.15')

    return float(temperature_in_celsius + 273.15)
