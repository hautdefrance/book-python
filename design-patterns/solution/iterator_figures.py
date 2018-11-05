for znak in 'python':
    print(znak)

for liczba in [1, 2, 3, 4]:
    print(liczba)

for key, value in [(0, 0), (1, 1), (1, 2)]:
    print('%s -> %s' % (key, value))

slownik = {'x': 1, 'y': 2}

for key in slownik:
    print(slownik.get(key))


class ListaFigurGeometrycznych:
    lista = []
    aktualny_elemtent = 0

    def __iter__(self):
        return self

    def push(self, figura):
        self.lista.append(figura)

    def next(self):
        self.aktualny_elemtent += 1
        return self.lista[self.aktualny_elemtent]
