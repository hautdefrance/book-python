class AddressBook:
    def __init__(self, kontakty=()):
        self.kontakty = kontakty

    def __str__(self):
        out = ', '.join(str(x) for x in self.kontakty)
        return f'[{out}]'


class Contact:
    def __init__(self, imie, nazwisko, adresy=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self):
        if not self.adresy:
            return f'{self.imie} {self.nazwisko}'
        else:
            out = ', '.join(str(x) for x in self.adresy)
            return f'{self.imie} {self.nazwisko} [{out}]'


class Address:
    def __init__(self, miasto=None, ulica=None, stan=None, kod=None, panstwo=None):
        self.miasto = miasto
        self.ulica = ulica
        self.stan = stan
        self.kod = kod
        self.panstwo = panstwo

    def __str__(self):
        return f'{self.miasto}'


melissa = Contact(imie='Melissa', nazwisko='Lewis')
print(melissa)
# Melissa Lewis

mark = Contact(imie='Mark', nazwisko='Watney', adresy=[Address(miasto='Houston'), Address(miasto='Cocoa Beach')])
print(mark)
# Mark Watney [Houston, Cocoa Beach]

addressbook = AddressBook([
    Contact(imie='Pan', nazwisko='Twardowski', adresy=[
        Address(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Address(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Address(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Address(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Contact(imie='José', nazwisko='Jiménez'),
    Contact(imie='Иван', nazwisko='Иванович', adresy=[]),
])


print(addressbook)
# [Pan Twardowski [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]
