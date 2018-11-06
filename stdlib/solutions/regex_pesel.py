import logging
import re

PESEL_REGEX = r'^\d{11}$'

log = logging.getLogger(__name__)


def poprawny_pesel(pesel):
    if re.match(PESEL_REGEX, pesel):
        return True
    else:
        return False


def czy_kobieta(pesel):
    """
    Sprawdzenie czy PESEL należy do kobiety.

    Przedostatni zank w PESEL oznacza płeć,
    gdy liczba jest parzysta, PESEL należy do kobiety,
    w przeciwnym wypadku numer jest mężczyzny.
    """

    if int(pesel[-2]) % 2 == 0:
        log.debug('Pesel należy do kobiety')
        return True
    else:
        log.debug('Pesel należy do mężczyzny')
        return False


if __name__ == '__main__':
    print('Moduł:', __name__)

    if czy_kobieta('12345678901'):
        print('Kobieta: tak')
    else:
        print('Kobieta: nie')