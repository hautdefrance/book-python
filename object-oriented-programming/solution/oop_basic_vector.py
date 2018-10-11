class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        return Vector(
            a=self.a + other.a,
            b=self.b + other.b,
            c=self.c + other.c
        )

    def __str__(self):
        return f'[{self.a}, {self.b}, {self.c}]'


v1 = Vector(1, 2, 3)
v2 = Vector(2, 5, 2)

v3 = v1 + v2

print(v3)