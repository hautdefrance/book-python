def decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@decorator
class X:
    pass


@decorator
class Y:
    pass


@decorator
class Z:
    pass


X.attr  # 100
Y.attr  # 100
Z.attr  # 100
