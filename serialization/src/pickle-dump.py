import pickle
from datetime import datetime, timezone, timedelta

FILENAME = 'filename.pkl'


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


with open(FILENAME, 'wb') as file:
    pickle.dump(DATA, file)
