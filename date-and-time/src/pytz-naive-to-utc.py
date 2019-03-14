from datetime import datetime
from pytz import utc


gagarin = datetime(1961, 4, 12, 14, 7)      # timezone naive


utc.localize(gagarin)
# datetime.datetime(1961, 4, 12, 14, 7, tzinfo=<UTC>)
