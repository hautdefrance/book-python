class Kontakt:
    def __init__(self, imie, nazwisko, adresy=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __iter__(self):
        self.obecny_adres = 0
        return self

    def __next__(self):
        if self.obecny_adres >= len(self.adresy):
            raise StopIteration

        adres = self.adresy[self.obecny_adres]
        self.obecny_adres += 1
        return adres


class Adres:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)


kontakt = Kontakt(imie='Matt', nazwisko='Kowalski', adresy=[
    Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas',
          kod='77058', panstwo='USA'),
    Adres(ulica=None, miasto='Kennedy Space Center', kod='32899',
          panstwo='USA'),
    Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109',
          panstwo='USA'),
    Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California',
          kod='93550', panstwo='USA'),
])


for adresy in kontakt:
    print(adresy)
