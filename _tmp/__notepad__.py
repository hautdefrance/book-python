class Person:
    def __init__(self, name=None, *args, **kwargs):
        self.name = name


class ABC(Person):
    def __init__(self, wiek=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wiek = wiek
        print(locals())

ABC(1, name='Jan', x=18)



def wyswietl(a, b, c=0):

    x = 1000
    y = 190123
    o = 'asdas'
    print(lambda: print(x)())

wyswietl(1, 2, 3)
