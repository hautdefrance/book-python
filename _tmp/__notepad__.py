class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __format__(self, format):
        if format == '2d':
            return f"({self.x}, {self.y})"
        elif format == '3d':
            return f"({self.x}, {self.y}, {self.z})"
        else:
            raise ValueError

p = Point(x=1, y=2)
print(f'{p:2d}')

