class MyClass:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None
