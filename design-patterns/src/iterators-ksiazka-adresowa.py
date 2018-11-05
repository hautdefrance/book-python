class Kontakt:
    def __init__(self, imie, nazwisko, adresy=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy


class Adres:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


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

for adres in kontakt:
    print(adres)
