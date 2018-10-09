import datetime
import json

DATA = """
{
    "astronaut":{
        "date": "1969-07-21",
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": "1961-05-05T14:34:13.000Z", "action": "launch"},
        {"datetime": "1961-05-05T14:49:35.000Z", "action": "landing"}
    ]
}
"""


class DatetimeDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.convert_datetime)

    def convert_datetime(slef, args):
        for key, value in args.items():

            if key == 'datetime':
                dt = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
                args['datetime'] = dt.replace(tzinfo=datetime.timezone.utc)

            elif key == 'date':
                dt = datetime.datetime.strptime(value, '%Y-%m-%d')
                args['date'] = dt.date()

        return args


out = json.loads(DATA, cls=DatetimeDecoder)
print(out)
