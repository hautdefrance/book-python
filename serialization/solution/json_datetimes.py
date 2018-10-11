import datetime
import json

FILENAME = '../tmp/json-datetimes.json'
DATA = {
    "datetime": datetime.datetime(1961, 4, 12, 2, 7, 0, 123456),
    "astronaut": {
        "date": datetime.date(1923, 11, 18),
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": datetime.datetime(1961, 5, 5, 14, 34, 13), "action": "launch"},
        {"datetime": datetime.datetime(1961, 5, 5, 14, 49, 35), "action": "landing"}
    ]
}


def encoder(self, obj):
    if isinstance(obj, datetime.datetime):
        return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'
    elif isinstance(obj, datetime.date):
        return f'{obj:%Y-%m-%d}'


def decoder(obj):
    for key, value in obj.items():
        if key == 'datetime':
            obj['datetime'] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        elif key == 'date':
            obj['date'] = datetime.datetime.strptime(value, '%Y-%m-%d').date()
    return obj


with open(FILENAME, mode='w', encoding='utf-8') as file:
    json.JSONEncoder.default = encoder
    json.dump(DATA, file)


with open(FILENAME, encoding='utf-8') as file:
    data = json.load(file, object_hook=decoder)


print(data)
