from typing import List, Dict


class Adres:
    def __init__(self, **kwargs: Dict[str, str]) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f'{self.__dict__}'

    def __repr__(self) -> str:
        return self.__str__()


class Kontakt:
    def __init__(self, imie: str, nazwisko: str, adresy: List[Adres] = []) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self) -> str:
        return f'{self.imie} {self.nazwisko} {self.adresy}'

    def __repr__(self) -> str:
        return self.__str__()



ksiazka_adresowa = [
    Kontakt(imie='Matt', nazwisko='Kowalski', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]

ivan = Kontakt(imie='Иван', nazwisko='Иванович', adresy=[Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA')])
print(ivan)
print(ksiazka_adresowa)
