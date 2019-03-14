from datetime import datetime, date
import json


DATA = {
    'email': 'jose.jimenez@nasa.gov',
    'date': date(1961, 4, 12),
    'datetime': datetime(1969, 7, 21, 14, 56, 15),
}


def encoder(self, value):

    if isinstance(value, datetime):
        format = '%Y-%m-%dT%H:%M:%S.%fZ'

    if isinstance(value, date):
        format = '%Y-%m-%d'

    return value.strftime(format)


json.JSONEncoder.default = encoder

output = json.dumps(DATA)
print(output)
# '{"email": "jose.jimenez@nasa.gov", "date": "1961-04-12", "datetime": "1969-07-21T14:56:15.000Z"}'
