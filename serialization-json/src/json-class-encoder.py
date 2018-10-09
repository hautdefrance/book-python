from datetime import datetime, date
import json


DATA = {
    'email': 'jose.jimenez@nasa.gov',
    'date': date(1961, 4, 12),
    'datetime': datetime(1969, 7, 21, 14, 56, 15),
}


class DatetimeEncoder(json.JSONEncoder):

    def default(self, value):
        if isinstance(value, datetime):
            return f'{value:%Y-%m-%dT%H:%M:%S.%fZ}'
        elif isinstance(value, date):
            return f'{value:%Y-%m-%d}'


output = json.dumps(DATA, cls=DatetimeEncoder)

print(output)
# {
#     "email": "jose.jimenez@nasa.gov",
#     "date": "1961-04-12",
#     "datetime": "1969-07-21T14:56:15.000000Z"
# }
