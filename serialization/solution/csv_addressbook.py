import csv


class Kontakt:
    def __init__(self, imie, nazwisko, adresy=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adresy}'

    def __repr__(self):
        return self.__str__()


class Adres:
    def __init__(self, **kwargs):
        self.ulica = kwargs.get('ulica', None)
        self.miasto = kwargs.get('miasto', None)

    def __str__(self):
        return f'{self.ulica} {self.miasto}'

    def __repr__(self):
        return self.__str__()


ksiazka_adresowa = [
    Kontakt(imie='Jan', nazwisko='Twardowski', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA', data_urodzenia=None),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]

do_zapisu = []

for kontakt in ksiazka_adresowa:
    adresy = []

    for adres in kontakt.adresy:
        dane = adres.__dict__.values()
        adres = '|'.join([str(x) for x in dane])
        adresy.append(adres)

    dane_kontaktu = kontakt.__dict__
    dane_kontaktu['adresy'] = ';'.join(adresy)
    do_zapisu.append(dane_kontaktu)


with open('filename.csv', 'w', encoding='utf-8') as file:
    fieldnames = set()
    for kontakt in do_zapisu:
        for fieldname in kontakt.keys():
            fieldnames.add(fieldname)


    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
    writer.writeheader()

    for row in do_zapisu:
        writer.writerow(row)
