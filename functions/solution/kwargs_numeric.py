def is_numeric(*args):
    for arg in args:

        if not isinstance(arg, (int, float)):
            return False

    return True
