from typing import List, Dict


class Address:
    def __init__(self, **kwargs: Dict[str, str]) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        miasto = getattr(self, 'miasto', 'n/a')
        return f'{miasto}'

    def __repr__(self) -> str:
        return self.__str__()


class Contact:
    def __init__(self, imie: str, nazwisko: str, adresy: List[Address] = []) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self) -> str:
        if self.adresy:
            return f'{self.imie} {self.nazwisko} {self.adresy}'
        else:
            return f'{self.imie} {self.nazwisko}'

    def __repr__(self) -> str:
        return self.__str__()


melissa = Contact(imie='Melissa', nazwisko='Lewis')
print(melissa)
# Melissa Lewis

mark = Contact(imie='Mark', nazwisko='Watney', adresy=[Address(miasto='Houston'), Address(miasto='Cocoa Beach')])
print(mark)
# Mark Watney [Houston, Cocoa Beach]

addressbook = [
    Contact(imie='Matt', nazwisko='Kowalski', adresy=[
        Address(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Address(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Address(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Address(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Contact(imie='José', nazwisko='Jiménez'),
    Contact(imie='Иван', nazwisko='Иванович', adresy=[]),
]


print(addressbook)
# [Matt Kowalski [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]
