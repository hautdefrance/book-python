from datetime import datetime
from pytz import utc


# timezone naive
gagarin = datetime(1961, 4, 12, 14, 7)


utc.localize(gagarin)
# datetime.datetime(1961, 4, 12, 14, 7, tzinfo=<UTC>)
