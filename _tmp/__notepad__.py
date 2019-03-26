class A:
    def show(self):
        print('a')


class B(A):
    def show(self):
        print('b')


class C(A):
    def show(self):
        print('c')


class D(B, C):
    pass


obj = D()

obj.show()
# b

print(D.__mro__)
# (<class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <class 'object'>)
