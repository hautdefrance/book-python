import pickle
from datetime import datetime, timezone, timedelta


def month_ago(dt):
    return dt - timedelta(days=30)


class Astronaut:
    agency = 'NASA'

    def __init__(self, name):
        self.name = name


jose = Astronaut(name='Jose Jimenez')
now = datetime.now(tz=timezone.utc)


DATA = [
    jose,
    Astronaut,
    month_ago(now),
    str(now),
    now.__str__(),
    '{}'.format(now),
    f'{now}',
    {'imie': 'Иван', 'nazwisko': 'Иванович'},
    {10, 20, 30},
    (1,),
    10,
    10.5,
]


output = pickle.dumps(DATA)
print(output)
# b'\x80\x03]q\x00(c__main__\nAstronaut\nq\x01)\x81q\x02}q\x03X\x04\x00\x00\x00nameq\x04X\x0c\x00\x00\x00Jose Jimenezq\x05sbh\x01cdatetime\ndatetime\nq\x06C\n\x07\xe2\t\x0b\r\n\x05\x04\xa9\xfdq\x07cdatetime\ntimezone\nq\x08cdatetime\ntimedelta\nq\tK\x00K\x00K\x00\x87q\nRq\x0b\x85q\x0cRq\r\x86q\x0eRq\x0fX \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x10X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x11X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x12X \x00\x00\x002018-10-11 13:10:05.305661+00:00q\x13}q\x14(X\x04\x00\x00\x00imieq\x15X\x08\x00\x00\x00\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbdq\x16X\x08\x00\x00\x00nazwiskoq\x17X\x10\x00\x00\x00\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb8\xd1\x87q\x18ucbuiltins\nset\nq\x19]q\x1a(K\nK\x14K\x1ee\x85q\x1bRq\x1cK\x01\x85q\x1dK\nG@%\x00\x00\x00\x00\x00\x00e.'
