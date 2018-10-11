#!/usr/bin/env python3


CONVERSION_TABLE = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'X': 10,
    'XX': 20,
    'XXX': 30,
    'XL': 40,
    'L': 50,
    'LX': 60,
    'LXX': 70,
    'LXXX': 80,
    'XC': 90,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_arabic(roman_value: str) -> int:
    """
    >>> roman_to_arabic("I")
    1
    >>> roman_to_arabic("IX")
    9
    >>> roman_to_arabic("MDL")
    1550
    >>> roman_to_arabic("XIV")
    14
    """
    roman_value.capitalize()
    arabic_value = []

    for letter in roman_value:
        if letter in CONVERSION_TABLE:
            arabic_value.append(CONVERSION_TABLE[letter])

    last_value = CONVERSION_TABLE["M"] * 2
    cumulative_value = 0

    for value in arabic_value:
        if last_value < value:
            cumulative_value -= 2 * last_value
        cumulative_value += value
        last_value = value

    return cumulative_value
