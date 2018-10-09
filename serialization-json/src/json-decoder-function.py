from datetime import datetime, date, timezone
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

def decoder(obj):
    for key, value in obj.items():

        if key == 'datetime':
            dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
            obj['datetime'] = dt.replace(tzinfo=timezone.utc)

        elif key == 'date':
            dt = datetime.strptime(value, '%Y-%m-%d')
            obj['date'] = dt.date()

        else:
            return obj


output = json.loads(DATA, object_hook=decoder)
print(output)
