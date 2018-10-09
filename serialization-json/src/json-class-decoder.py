import datetime
import json


DATA = """
{
    "email": "jose.jimenez@nasa.gov",
    "date": "1961-04-12",
    "datetime": "1969-07-21T14:56:15.000Z"
}
"""


class DatetimeDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.convert_datetime)

    def convert_datetime(slef, obj):
        for key, value in obj.items():

            if key == 'datetime':
                dt = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                obj['datetime'] = dt.replace(tzinfo=datetime.timezone.utc)

            elif key == 'date':
                dt = datetime.datetime.strptime(value, '%Y-%m-%d')
                obj['date'] = dt.date()

        return obj


output = json.loads(DATA, cls=DatetimeDecoder)

print(output)
# {
#     'email': 'jose.jimenez@nasa.gov',
#     'date': date(1961, 4, 12),
#     'datetime': datetime(1969, 7, 21, 14, 56, 15, tzinfo=datetime.timezone.utc),
# }
