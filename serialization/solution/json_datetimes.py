from datetime import datetime, date
import json

FILENAME = '../tmp/json-datetimes.json'
DATA = {
    "astronaut": {
        "date": date(1961, 4, 12),
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": datetime(1969, 7, 21, 14, 56, 15), "action": "landing"}
    ]
}


def encoder(self, obj):
    if isinstance(obj, datetime):
        return f'{obj:%Y-%m-%dT%H:%M:%S.%fZ}'
    elif isinstance(obj, datetime.date):
        return f'{obj:%Y-%m-%d}'


def decoder(obj):
    for key, value in obj.items():
        if key == 'datetime':
            obj['datetime'] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        elif key == 'date':
            obj['date'] = datetime.strptime(value, '%Y-%m-%d').date()
    return obj


with open(FILENAME, mode='w', encoding='utf-8') as file:
    json.JSONEncoder.default = encoder
    json.dump(DATA, file)


with open(FILENAME, encoding='utf-8') as file:
    data = json.load(file, object_hook=decoder)


print(data)
