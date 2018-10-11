import datetime
import json


def datetime_encoder(self, obj):
    if isinstance(obj, datetime.date):
        return f'{obj:%Y-%m-%d}'
    else:
        return str(obj)

json.JSONEncoder.default = datetime_encoder

data = {"datetime": datetime.date(1961, 4, 12)}
json.dumps(data)
# {"datetime": "1961-04-12"}