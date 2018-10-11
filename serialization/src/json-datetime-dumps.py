from datetime import datetime, date
import json


DATA = {
    'email': 'jose.jimenez@nasa.gov',
    'date': date(1961, 4, 12),
    'datetime': datetime(1969, 7, 21, 14, 56, 15),
}

output = json.dumps(DATA)
# TypeError: Object of type date is not JSON serializable
