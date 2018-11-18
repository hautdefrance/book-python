class AddressBook:
    def __init__(self, kontakty=()):
        self.kontakty = kontakty


class Address:
    def __init__(self, ulica=None, miasto=None, stan=None, kod=None, panstwo=None):
        self.ulica = ulica
        self.miasto = miasto
        self.stan = stan
        self.kod = kod
        self.panstwo = panstwo

    def __str__(self):
        return str(self.miasto)

    def __repr__(self):
        return self.__str__()


class Contact:
    def __init__(self, imie, nazwisko, adresy=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adresy}'



melissa = Contact(imie='Melissa', nazwisko='Lewis')
print(melissa)
# Melissa Lewis

mark = Contact(imie='Mark', nazwisko='Watney', adresy=[Address(miasto='Houston'), Address(miasto='Cocoa Beach')])
print(mark)
# Mark Watney [Houston, Cocoa Beach]

addressbook = AddressBook([
    Contact(imie='Matt', nazwisko='Kowalski', adresy=[
        Address(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Address(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Address(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Address(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Contact(imie='José', nazwisko='Jiménez'),
    Contact(imie='Иван', nazwisko='Иванович', adresy=[]),
])







"""
jose = Kontakt(imie='Jose', nazwisko='Jimenez')
jsc = Adres(ulica='2101 E NASA Pkwy', kod='77058', miasto='Houston', stan='Texas', kraj='USA')
jose.adres.append(jsc)


ivan = Kontakt(imie='Ivan', nazwisko='Ivanovich')

print(ivan.adres)
"""
