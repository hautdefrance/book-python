import json
import logging
import pickle

KSIAZKA_ADRESOWA_PICKLE = 'ksiazka-adresowa.pickle'

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Kontakt:
    def __init__(self, imie, nazwisko, telefon=None, adresy=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.adresy = adresy

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adresy}'

    def __repr__(self):
        return self.__str__()


class Adres:
    def __init__(self, **kwargs):
        # self.ulica = kwargs.get('ulica', None)
        # self.miasto = kwargs.get('miasto', None)
        for var, value in kwargs.items():
           setattr(self, var, value)

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



log.debug(f'Ksiażka adresowa: {ksiazka_adresowa}')


with open(KSIAZKA_ADRESOWA_PICKLE, mode='wb') as file:
    serialized = pickle.dumps(ksiazka_adresowa)
    file.write(serialized)


with open(KSIAZKA_ADRESOWA_PICKLE, mode='rb') as file:
    unserialized = pickle.loads(file.read())
    log.debug(f'Pickle: {unserialized}')


class JSONObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return obj.__dict__


class JSONObjectDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_object)

    def decode_object(self, dictionary):
        if dictionary.get('miasto'):
            return Adres(**dictionary)
        else:
            return Kontakt(**dictionary)


with open('/_tmp/ksiazka-adresowa.json', 'w') as file:
    serialized = json.dumps(ksiazka_adresowa, cls=JSONObjectEncoder)
    file.write(serialized)


with open('/_tmp/ksiazka-adresowa.json', 'r') as file:
    unserialized = json.loads(file.read(), cls=JSONObjectDecoder)
    log.debug(f'JSON: {unserialized}')
