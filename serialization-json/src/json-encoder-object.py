import json
from dataclasses import dataclass


@dataclass
class Adres:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


@dataclass
class Kontakt:
    imie: str
    nazwisko: str
    adresy: tuple = ()


ksiazka_adresowa = [
    Kontakt(imie='Matt', nazwisko='Kowalski', adresy=(
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    )),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=()),
]


class KontaktEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return {
                "type": obj.__class__.__name__,
                "fields": obj.__dict__
            }


out = json.dumps(ksiazka_adresowa, cls=KontaktEncoder)
print(out)
