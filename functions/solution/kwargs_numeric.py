def is_numeric(*args):
    if not args:
        return None

    for arg in args:

        if not isinstance(arg, (int, float)):
            return False

    return True
