#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest


class Prostokat:

    def __init__(self, a, b):
        """
        >>> Prostokat(0, 1)
        Traceback (most recent call last):
        ...
        ValueError: Długość boku musi być dodatnia
        """
        self.a = a
        self.b = b
        self.c = 10

        if a <= 0 or b <= 0:
            raise ValueError('Długość boku musi być dodatnia')

    def pole(self) -> int:
        """
        Wyświtla pole dla danej figury
        """
        return self.a * self.b

    def obwod(self) -> int:
        """
        Wyświtla obwod dla danej figury
        """
        return (self.a + self.b) * 2

    def __str__(self):
        # return 'Prostokat({a}, {b})'.format(**self.__dict__)
        return 'Prostokat({a}, {b})'.format(**vars(self))

class ProstokatTest(unittest.TestCase):

    def setUp(self):
        self.prostokat_1_na_4 = Prostokat(1, 4)
        self.prostokat_2_na_5 = Prostokat(2, 5)

    def test_bok_a(self):
        self.assertEquals(self.prostokat_1_na_4.a, 1)
        self.assertEquals(self.prostokat_2_na_5.a, 2)

    def test_bok_b(self):
        self.assertEquals(self.prostokat_1_na_4.b, 4)
        self.assertEquals(self.prostokat_2_na_5.b, 5)

    def test_ujemna_bok_a(self):
        with self.assertRaises(ValueError):
            Prostokat(-1, 5)

    def test_ujemny_bok_b(self):
        with self.assertRaises(ValueError):
            Prostokat(5, -1)

    def test_zerowa_bok_a(self):
        with self.assertRaises(ValueError):
            Prostokat(0, 1)

    def test_zerowy_bok_b(self):
        with self.assertRaises(ValueError):
            Prostokat(1, 0)

    def test_nieprawidlowa_wartosc_boku(self):
        with self.assertRaises(TypeError):
            Prostokat('trzy', 0)

    def test_pole(self):
        self.assertEquals(Prostokat(2, 5).pole(), 10)
        self.assertEquals(Prostokat(1, 4).pole(), 4)

    def test_pole_setup(self):
        self.assertEquals(self.prostokat_1_na_4.pole(), 4)
        self.assertEquals(self.prostokat_2_na_5.pole(), 10)

    def test_obwod_positive(self):
        self.assertEquals(Prostokat(2, 5).obwod(), 14)
        self.assertEquals(Prostokat(1, 4).obwod(), 10)

    def test_obwod_negative(self):
        self.assertNotEquals(Prostokat(2, 5).obwod(), 10)
        self.assertNotEquals(Prostokat(1, 4).obwod(), 5)
