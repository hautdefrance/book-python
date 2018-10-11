from pprint import pprint


class A:
    def wyswietl(self):
        print('a')


class B:
    def wyswietl(self):
        print('b')


class C:
    def wyswietl(self):
        print('c')


class D(A, B, C):
    pass


d = D().wyswietl()  # a

pprint(D.__mro__)
# (<class '__main__.D'>,
#  <class '__main__.A'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class 'object'>)