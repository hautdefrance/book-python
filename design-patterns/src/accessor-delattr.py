class Point:
    x = 10
    y = -5
    z = 0

    def __delattr__(self, name):
        if name == 'z':
            raise ValueError('Cannot delete field')
        else:
            super().__delattr__(name)

p = Point()

del p.y
delattr(p, 'z')
