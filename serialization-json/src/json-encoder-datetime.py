from datetime import datetime, date
import json


DATA = {
    "astronaut": {
        "date": date(1969, 7, 21),
        "person": "jose.jimenez@nasa.gov"
    },
    "flight": [
        {"datetime": datetime(1961, 5, 5, 14, 34, 13), "action": "launch"},
        {"datetime": datetime(1961, 5, 5, 14, 49, 35), "action": "landing"}
    ]
}


def encoder(self, value):

    if isinstance(value, datetime):
        return f'{value:%Y-%m-%dT%H:%M:%S.%fZ}'

    elif isinstance(value, date):
        return f'{value:%Y-%m-%d}'


json.JSONEncoder.default = encoder

out = json.dumps(DATA)
print(out)
# {
#   "astronaut": {
#       "date": "1969-07-21",
#       "person": "jose.jimenez@nasa.gov"
#   },
#   "flight": [
#       {"datetime": "1961-05-05T14:34:13.000000Z", "action": "launch"},
#       {"datetime": "1961-05-05T14:49:35.000000Z", "action": "landing"}
#   ]
# }
