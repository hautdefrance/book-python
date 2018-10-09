from datetime import datetime
import json

DATA = {"datetime": datetime(1961, 4, 12, 2, 7, 0, 123456)}

json.dumps(DATA)
# TypeError: Object of type 'datetime' is not JSON serializable
