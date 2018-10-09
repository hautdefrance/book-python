from unittest import TestCase

BOUNDARY_X_MIN = 0
BOUNDARY_X_MAX = 1024


class Dragon:
    def __init__(self, name, position_x=0, position_y=0):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y

    def set_position(self, x, y):
        if not BOUNDARY_X_MIN < x < BOUNDARY_X_MAX:
            raise ValueError(_('Out of bounds'))

        self.position_x = x
        self.position_y = y

    def move(self, left=0, right=0):
        self.set_position(
            x=self.position_x + right - left,
            y=0
        )


class DragonTest(TestCase):

    def setUp(self):
        self.smok = Dragon(name="Wawelski", position_x=100, position_y=50)

    def test_create_dragon(self):
        wawelski = Dragon(name="Wawelski")
        self.assertEqual(wawelski.name, "Wawelski")

    def test_position_xy(self):
        self.assertEqual(self.smok.position_x, 100)
        self.assertEqual(self.smok.position_y, 50)

    def test_set_position(self):
        self.smok.set_position(x=10, y=20)
        self.assertEqual(self.smok.position_x, 10)
        self.assertEqual(self.smok.position_y, 20)

    def test_move(self):
        self.smok.move(left=10)
        self.assertEqual(self.smok.position_x, 90)

        self.smok.move(right=10)
        self.assertEqual(self.smok.position_x, 100)

    def test_boundary(self):
        with self.assertRaises(ValueError):
            self.smok.move(left=500)

        with self.assertRaises(ValueError):
            self.smok.set_position(x=BOUNDARY_X_MAX + 1, y=0)
